import json
import sqlite3

def Jsondb(lista):
               
               DB_FILE = "some.db"

               conn = sqlite3.connect(DB_FILE)

               c = conn.cursor()
               try:
                              c.execute('create table Employees (emailAddress, employeeCode,firstName,jobTitle,lastName,phoneNumber,region,userId)')
               except:
                              pass
               for x in lista['Employees']:
                              query = "insert into Employees values('" + x['emailAddress']+ "','"+ x['employeeCode']+"','"+ x['firstName']+"','"+x['jobTitle'] +"','"+ x['lastName']+"','"+x['phoneNumber']+"','"+ x['region']+"','"+ x['userId']+"')"
                              c.execute(query)

               conn.commit()
               c.close()

def carregarDB():
               data = {}
               data['Employees'] = []
               DB_FILE = "some.db"
               conn = sqlite3.connect(DB_FILE)
               c = conn.cursor()
               query = "SELECT * from Employees"
               for x in c.execute(query):
                              data['Employees'].append( 
                                             {
                                             "userId": x[7],
                                             "jobTitle": x[3],
                                             "firstName":x[2],
                                             "lastName": x[4],
                                             "employeeCode": x[1],
                                             "region": x[6],
                                             "phoneNumber": x[5],
                                             "emailAddress": x[0]
                                             }
                              )
               c.close()
               return data
def leerJson(lista):
               with open('copia.json', 'r') as json_file: 
                              data = json.load(json_file) 

               return data


def GuardarEnJson(lista):
               with open('copia.json', 'w') as f:
                              json.dump(lista,f,indent=4)


def adicionarElemnto(data):                                         
               data['Employees'].append( 
                              {
                              "userId": input("userid: "),
                              "jobTitle": input("jobTitle: "),
                              "firstName":input("firstName: "),
                              "lastName": input("lastName"),
                              "employeeCode": input("employeeCode: "),
                              "region": input("Region: "),
                              "phoneNumber": input("phoneNumber: "),
                              "emailAddress": input("emailAddress: ")
                              }
               )

def procurarChave(data):
               chave = input("Chave: ")
               x = input("Valor: ")
               for k in data['Employees']:
                              if(k[chave] == x):
                                             print(k[chave])


def main():
               try:
                              with open('copia.json', 'r') as file:
                                             lista = json.load(file)
               except:
                              lista = {}
                              pass


               while(True):
                              a = input("Menu:\na.leer ficheiro json\nb. grabar\nc. listar a variables\nd.adicionar elemento \ne. Procurar por chave\ndb.guardar ficheiro em db \nldb. leer base de datos\n  >")

                              if a  == "a":
                                             lista = leerJson(lista)

                              if a  == "b":
                                             pass

                              if a  == "c":
                                             print(lista)

                              if a  == "d":
                                             adicionarElemnto(lista)
                              
                              if a  == "e":
                                             procurarChave(lista)
                              
                              if a  == "db":
                                             Jsondb(lista)

                              if a  == "ldb":
                                             lista = carregarDB()



if __name__ == '__main__':
               main()
