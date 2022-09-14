import json
import sqlite3
import os
import fileinput
from sqlite3.dbapi2 import Row
import xlsxwriter
import pandas as pd

SQLiteDatabase = "SQLite.db"

def querySQL(query):
               conn = sqlite3.connect(SQLiteDatabase)
               c = conn.cursor()
               x = None
               try:
                              x = c.execute(query)
                              conn.commit()
               except Exception as e:
                              print(e)
               return x

class Contacto:
               Nome = ""
               Numero_Telefone = 0
               Morada = ""
               def __init__(self,Nome, Numero_Telefone,Morada,):
                              self.Nome = Nome
                              self.Numero_Telefone = Numero_Telefone
                              self.Morada = Morada
               
               def __str__(self):
                              return self.Nome + " , " + str(self.Numero_Telefone) + " , " + self.Morada
               def __repr__(self):
                              return str(self)
               
               def registar(self):
                              querySQL("INSERT INTO Contacto VALUES(" + str(self.Numero_Telefone) + ",'" + self.Nome + "','" + self.Morada + "')")


               @staticmethod
               def criar_tabela():
                              querySQL('''
                                             CREATE TABLE IF NOT EXISTS contacto (
                                                            Numero_Telefone integer PRIMARY KEY,
                                                            Nome text NOT NULL,
                                                            Morada text
                                             );
                              ''')
               @staticmethod
               def get_all_contactos():
                              l = []
                              for x in querySQL("SELECT * from contacto "):
                                             l.append(Contacto(x[1],x[0],x[2]))
                              return l
               
               
class Ligacoes:
               Origen = 0
               Destino = 0
               def __init__(self,Origen,Destino):
                              self.Origen = Origen
                              self.Destino = Destino
               def __str__(self):
                              return str(self.Origen) + " , " + str(self.Destino)

               def __repr__(self):
                              return str(self)

               def registar(self):
                              querySQL("INSERT INTO Ligacoes VALUES('" + str(self.Origen) + "','" + str(self.Destino) + "')")

               @staticmethod
               def get_all_ligacoes():
                              l = []
                              for x in querySQL("SELECT * from ligacoes "):
                                             l.append(Ligacoes(x[0],x[1]))
                              return l

               @staticmethod
               def criar_tabela_ligacoes():
                              querySQL('''
                                             CREATE TABLE IF NOT EXISTS Ligacoes (
                                             Origem integer ,
                                             Destino integer ,
                                             PRIMARY KEY (Origem, Destino),
                                             FOREIGN KEY (Origem) REFERENCES contacto(Numero_Telefone),
                                             FOREIGN KEY (Destino) REFERENCES contacto(Numero_Telefone)
                                             );
                              ''')

def SQLToJson():
               data = { 'Contacto' : []}

               for x in querySQL("SELECT * from Contacto"):
                              ll = []
                              for k in querySQL("SELECT * from Ligacoes"):
                                             if k[0] == x[0]:
                                                            ll.append(k[1])
                              data['Contacto'].append(
                                             {
                                             "Numero_Telefone": x[0],
                                             "Nome": x[1],
                                             "Morada": x[2],
                                             "Ligacoes": ll
                                             }
                              )
               

               with open('Contacto_Ligacoes.json', 'w') as f:
                              json.dump(data,f,indent=4)
                                  
def JsonToSQLite():
               SQLiteDatabase = "SQLite.db"
               try:
                              os.remove(SQLiteDatabase)
               except:
                              pass

               x = "Contacto_Ligacoes.json"
               with open(x, "r") as json_file:
                              data = json.load(json_file)
                              Contacto.criar_tabela()
                              Ligacoes.criar_tabela_ligacoes()
                              
                              for x in data["Contacto"]:
                                             novo_contacto = Contacto(x["Nome"],x["Numero_Telefone"],x["Morada"])
                                             novo_contacto.registar()
                                             for y in x["Ligacoes"]:
                                                            nova_ligacao = Ligacoes(x["Numero_Telefone"],y)
                                                            nova_ligacao.registar()
                              
#convertir Base de dados para Excel 
def SQLiteToExcel():
               workbook = xlsxwriter.Workbook('BaseDadosExcel.xlsx')
               worksheet = workbook.add_worksheet()

               
               row = 0
               col = 0
               worksheet.write(row, col, "Nome")
               worksheet.write(row, col+1, "Numero Telefone")
               worksheet.write(row, col+2, "Morada")
               row += 1
               for c in Contacto.get_all_contactos():
                              worksheet.write(row, col, c.Nome)
                              worksheet.write(row, col + 1, c.Numero_Telefone)
                              worksheet.write(row, col + 2, c.Morada)
                              row += 1


               worksheet = workbook.add_worksheet()
               row = 0 
               col = 0

               worksheet.write(row, col, "Origem")
               worksheet.write(row, col+1, "Destino")
               row += 1
               for z in Ligacoes.get_all_ligacoes():
                              worksheet.write(row, col,     z.Origen)
                              worksheet.write(row, col +1, z.Destino)

                              row += 1
               workbook.close()

def ExcelToJson():
               JsonDataBase = "Contacto_Ligacoes.json"
               ret = []
               try:
                              os.remove(JsonDataBase)
               except:
                              pass

               cc = pd.read_excel('BaseDadosExcel.xlsx',sheet_name=0).values.tolist()
               ll = pd.read_excel('BaseDadosExcel.xlsx',sheet_name=1).values.tolist()

               print(cc)
               print(ll)

               for c in cc:
                              elem = {}
                              elem['Numero_Telefone'] = c[1]
                              elem['Nome'] = c[0]
                              elem['Morada'] = c[2]
                              elem['Ligacoes'] = []

                              for l in ll:
                                             if l[0] == c[1]:
                                                            elem['Ligacoes'].append(l[1])
                              ret.append(elem)

               print(ret)

               with open('Contacto_Ligacoes.json', 'w') as f:
                              json.dump(ret,f,indent=4)
               
                              
 
def main():
               l = []
               lista_ligacoes = []
               db = "SQLiteDatabase.db"

               if os.path.exists(db) == False:
                              Contacto.criar_tabela()
                              Ligacoes.criar_tabela_ligacoes()

               

               while True:
                              i = input("Menu:\n\t1. Adicionar Contacto\n\t2. Listar contacto\n\t3. Procurar contacto\n\t4 Adionar Ligacao \n\t5 Ver Ligacoes \n\t6 Exportar SQLdatabase to Json\n\t7 Eliminar SQliteBD y gerar com o novo Json \n\t8 Geral de SQL a Excel \n\t9 Geral de Excel para Json \n\t\0. Sair\n>")

                              if i == "1":
                                             c = Contacto(input("Nome: "), input("Numero_Telefone: "), input("Morada: "))
                                             c.registar()
                                             l.append(c)
                                             pass
                              elif i == "2":
                                             for x in Contacto.get_all_contactos():
                                                            print(x)
                              elif i == "3":
                                             nome = input("Nome: ")
                                             for x in l:
                                                            if x[0] == nome:
                                                                           print("Nome: " + x[0] + ", Numero_Telefone: " + x[1] + ", Morada: " + x[2])
                              elif i  == "4":
                                             c = Ligacoes(input("Origen: ") , input("Destino: "))
                                             c.registar()
                                             lista_ligacoes.append(c)
                                             pass

                              elif i == "5":
                                             for x in Ligacoes.get_all_ligacoes():
                                                            print(x)
                                             pass

                              elif i == "6":
                                             SQLToJson()
                                             pass
                              elif i == "7":
                                             JsonToSQLite()
                                             pass
                              elif i == "8":
                                             SQLiteToExcel()
                                             pass
                              elif i == "9":
                                             ExcelToJson()
                                             pass
                              elif i == "0":
                                             break
                              else:
                                             print("Opcao errada!")



if __name__ == '__main__':
                   main()
    
                   
