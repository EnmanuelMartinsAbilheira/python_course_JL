import json
import sqlite3

basedados = "ex3.db"

def querySQL(query):
               conn = sqlite3.connect(basedados)
               c = conn.cursor()
               x = None
               
               try:
                              x = c.execute(query)
                              conn.commit()
               except Exception as e:
                              print(e)

               return x

class pessoa():
               Nome = ""
               UserId = ""
               idade = 0
               password=""
               def __init__(self, Nome,userId ,idade,password):
                              self.Nome = Nome
                              self.UserId = userId
                              self.idade = idade
                              self.password = password
               
               def __str__(self):
                              return self.Nome + " , " + str(self.UserId) + " , " + str(self.idade)

               def registar(self):
                              querySQL("INSERT INTO pessoa VALUES('" + self.Nome + "','"+self.UserId + "'," + str(self.idade) + ",'" + self.password + "')")


               @staticmethod
               def form_criar_utilizador():
                              pessoa(
                                             input("Introduza nome: "),
                                             input("User ID: "),
                                             int(input("idade: ")),
                                             input("Password: ")
                              ).registar()
               @staticmethod
               def listar_utilizadores():
                              for x in querySQL("SELECT * from pessoa"):
                                             print(x)

               @staticmethod
               def login():
                              for x in querySQL("SELECT * from pessoa where pessoa.UserId='"+input("UserID: ") +"' and pessoa.Password='"+input("Password: ")+"'"):
                                             return pessoa(x[0],x[1],x[2],x[3])
                              return None

class receitas(): 
               nome = ""
               ListIngredientes = ""
               IdReceita = ""
               def __init__(self,nome, ListIngredientes, IdReceita):
                              self.nome = nome
                              self.ListIngredientes = ListIngredientes
                              self.IdReceita = IdReceita
               
               def __str__(self):
                              return self.nome + " , " + str(self.ListIngredientes)+ " , " + str(self.IdReceita)


               
               def registar(self):
                              querySQL ("INSERT INTO Receitas VALUES ('" + self.nome + "','" + self.ListIngredientes + "','" + self.IdReceita + "')")

               @staticmethod
               def form_criar_Receita():
                              receitas(
                                             input("Introduza nome: "),
                                             input("lista de ingredientes: "),
                                             input("ID Receita: ")
                              ).registar()
                              
               @staticmethod
               def listar_receitas():
                              for x in querySQL("SELECT * from Receitas"):
                                             print(x)
                                  


class InserirPassos(): 
               Describcao = ""
               IdPassos = ""
               NumeroPassos = ""
               IdReceita = ""
               def __init__(self,Describcao, IdPassos, NumeroPassos, IdReceita):
                              self.Describcao = Describcao
                              self.IdPassos = IdPassos
                              self.NumeroPassos = NumeroPassos
                              self.IdReceita = IdReceita
               
               def __str__(self):
                              return self.Describcao + " , " + self.IdPassos+ " , " + self.NumeroPassos+ " , " + self.IdReceita


               
               def registar(self):
                              querySQL(" INSERT INTO InserirPassos VALUES('" + self.Describcao + "','" + self.IdPassos + "','" + self.NumeroPassos + "," + self.IdReceita + "') ")



               @staticmethod
               def form_criar_InserirPassos():
                              InserirPassos(
                                             input("Introduza Describcao: "),
                                             input("IdPassos: "),
                                             input("Numeropasso: "),
                                             input("ID Receita: ")
                              ).registar()
                              
               @staticmethod
               def listar_InserirPassos():
                              for x in querySQL("SELECT * from Inserirpassos"):
                                             print(x)
                                  




class Ingredientes():              
               IdReceita = ""
               IdIngredente = ""
               NomeIngredente = ""
  
               def __init__(self,NomeIngredente, IdIngredente, IdReceita):
                              self.NomeIngredente = NomeIngredente
                              self.IdIngredente = IdIngredente
                              self.IdReceita = IdReceita
               
               def __str__(self):
                              return str(self.IdReceita)  + " , " + str(self.IdIngredente)+ " , " + self.NomeIngredente


               
               def registar(self):
                              querySQL ("INSERT INTO Ingredientes VALUES ('" + self.IdReceita + "','" + self.IdIngredente + "','" + self.NomeIngredente + "')")



               @staticmethod
               def form_criar_ingredentes():
                              Ingredientes(
                                             input("Introduza Id da receita: "),
                                             input("introducir Id do ingredente: "),
                                             input("introducir os nome dos ingredentes: ")
                              ).registar()
                              
               @staticmethod
               def listar_Ingredientes():
                              for x in querySQL("SELECT * from Ingredientes"):
                                             print(x)
                                  



def main():
               p = None 
               while(True):
                              a = input("Menu:\na.Registrar Utilizadores\nb.Ver Utilizadores\nc.login utilizador\ne. registrar receita\nf.ver receitas\ng. registrar inserir passos \nh.ver passos inseriros \ni.crear ingredientes \nj.ver todos los ingredientes \n >")
                              if a=="a":
                                             pessoa.form_criar_utilizador()
                              if a=="b":
                                             pessoa.listar_utilizadores()
                              if a=="c":
                                             p = pessoa.login()
                              if a =="e":
                                             if p != None:
                                                            receitas.form_criar_Receita()
                              if a =="f":
                                             if p != None:
                                                            receitas.listar_receitas()
                                             
                              if a =="g":
                                             InserirPassos.form_criar_InserirPassos()
                              
                              if a =="h":
                                             InserirPassos.listar_InserirPassos()

                              if a =="i":
                                             Ingredientes.form_criar_ingredentes()
                              
                              if a =="j":
                                             Ingredientes.listar_Ingredientes()


if __name__ == '__main__':
               main()