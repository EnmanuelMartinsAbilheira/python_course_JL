import json
import sqlite3


class pessoa():
               Nome = ""
               UserId = ""
               idade = 0
               def __init__(self, Nome,userId ,idade):
                              self.Nome = Nome
                              self.userId = userId
                              self.idade = idade
               
               def __str__(self):
                              return self.Nome + " , " + str(self.userId) + " , " + str(self.idade)

class receitas():
               
               
               nome = ""
               ListIngredientes = ""
               ListPasos = ""
               def __init__(self,nome, ListIngredientes, ListPasos):
                              self.nome = nome
                              self.ListIngredientes = ListIngredientes
                              self.ListPasos = ListPasos
               
               def __str__(self):
                              return self.nome + " , " + str(self.ListIngredientes)+ " , " + str(self.ListPasos)

def ler_Tables():
               data = {}
               data['Tables'] = []
               DB_FILE = "ex3.db"
               conn = sqlite3.connect(DB_FILE)
               c = conn.cursor()
               query = "SELECT * from Tables"
               for x in c.execute(query):
                              
                              data['Tables'].append( 
                                             [

                                                            data['Ingredientes'].append(
                                                                           {
                                                                           "IdReceita": x[0],
                                                                           "IdIngredente": x[1],
                                                                           "NomeIngredente":x[2]
                                                                           }
                                                            ),

                                                            data['InserirPassos'].append(
                                                                           {
                                                                           "Describcao": x[0],
                                                                           "IdPassos": x[1],
                                                                           "NumeroPasso":x[2],
                                                                           "IdReceita": x[3]
                                                                           }
                                                            ),

                                                            data['Receitas'].append(
                                                                           {
                                                                           "Nome": x[0],
                                                                           "ListIngrediente": x[1],
                                                                           "IdReceita":x[2]
                                                                           }
                                                            ),

                                                            data['pessoa'].append(
                                                                           {
                                                                           "Nome": x[0],
                                                                           "UserId": x[1],
                                                                           "Idade":x[2],
                                                                           "Password": x[3]
                                                                           }
                                                            )

                                             ]
                              )

                              print(x)
               c.close()
               return data

def inserirPessoa(data):
               
               # conn = sqlite3.connect('ex3.db')
               # print('Connected to database successfully.')

               # cur = conn.cursor()
               # pessoa = ("Nome", "UserId", "Idade", "Password")
               # cur.execute("inserir valores da pessoa(Nome, UserId, Idade, Password) values(?, ?, ?, ?)", pessoa)
             
               # print('Records inserted successfully.')
               
               # conn.commit()
               # conn.close()
               
               data['Tables'].append(                         
                              data['pessoa'].append( 
                                             {
                                             "Nome": input("Nome: "),
                                             "UserId": input("UserId: "),
                                             "Idade":input("Idade: "),
                                             "Password": input("Password: ")
                                             }
                              )
               )

def inserirReceitas(data):
               
               # conn = sqlite3.connect('ex3.db')
               # print('Connected to database successfully.')
               
               # cur = conn.cursor()
               # Receitas = ("Nome", "ListIngrediente", "IdReceita")
               # cur.execute("inserir valores da Receitas(Nome, ListIngrediente, IdReceita) values(?, ?, ?)", Receitas)
              
               # print('Records inserted successfully.')
               
               # conn.commit()
               # conn.close()

                                 
               data['Receitas'].append( 
                              {
                              "Nome": input("Nome: "),
                              "ListIngrediente": input("ListIngrediente: "),
                              "IdReceita":input("IdReceita: ")
                              }
               )

def inSErirPasos(data):
               # conn = sqlite3.connect('ex3.db')
               # print('Connected to database successfully.')
               
               # cur = conn.cursor()
               # InserirPassos = ("Describcao", "IdPassos", "NumeroPasso", "IdReceita")
               # cur.execute("inserir valores dos Passos(Describcao, IdPassos, NumeroPasso, IdReceita) values(?, ?, ?, ?)", InserirPassos)
               
               # print('Records inserted successfully.')
               
               # conn.commit()
               # conn.close()
                             
               data['InserirPassos'].append( 
                              {
                              "Describcao": input("Describcao: "),
                              "IdPassos": input("IdPassos: "),
                              "NumeroPasso":input("NumeroPasso: "),
                              "IdReceita": input("IdReceita: ")
                              }
               )

def inserirIngredientes(data):
                              
               # conn = sqlite3.connect('ex3.db')
               # print('Connected to database successfully.')
               
               # cur = conn.cursor()
               # Ingredientes = ("IdReceita", "IdIngredente", "NomeIngredente")
               # cur.execute("inserir valores dos Ingredientes(IdReceita, IdIngredente, NomeIngredente) values(?, ?, ?)", Ingredientes)
               
               # print('Records inserted successfully.')
               
               # conn.commit()
               # conn.close()

           
               data['Ingredientes'].append( 
                              {
                              "IdReceita": input("IdReceita: "),
                              "IdIngredente": input("IdIngredente: "),
                              "NomeIngredente":input("NomeIngredente: ")
                              }
               )

def registarUtilizador():
               

def main():
               
 

               while(True):
                              a = input("Menu:\na.registrar utilizadores \nb.Login Utilizadores\nc.Criar receita\nd. Procurar receita de outro utilizadores\n  >")

                              if a  == "a":


                              # if a  == "b":                                      

                              # if a  == "c":
                                             

                              # if a  == "d":
                                             



if __name__ == '__main__':
               main()
