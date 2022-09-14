import pickle
import json
class Funcionario:
               Nome = ""
               idade = 0
               Salario = 0

               def default(self,o):
                              return o.__dict__

               def toJSON(self):
                       return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
               
               def __init__(self,Nome, idade, Salario):
                              self.Nome = Nome
                              self.idade = idade
                              self.Salario = Salario

               def __repr__(self):
                              return str(self) 
               def __str__(self):
                              return "[" + self.Nome + " , " + str(self.idade) + " , " + str(self.Salario) + "]"

class Medico(Funcionario):
               
               def __init__(self, f, Lista_Especialidade, Ano_Exp):
                              super().__init__(f.Nome,f.idade,f.Salario)
                              self.Lista_Especialidade = Lista_Especialidade
                              self.Ano_Exp = Ano_Exp
               def toJSON(self):
                              return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
               def __repr__(self):
                              return str(self)
               def __str__(self):
                              return "[" + super().__str__() + " , " + str(self.Lista_Especialidade) + " , " + str(self.Ano_Exp) + "]"           

class Enfermeiro(Funcionario):
               def __init__(self, f, Ano_Exp):
                              super().__init__(f.Nome,f.idade,f.Salario)
                              self.Ano_Exp = Ano_Exp
               def __repr__(self):
                              return str(self)
               def toJSON(self):
                              return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
               def __str__(self):
                              return "[" + super().__str__() + " , " + str(self.Ano_Exp) + "]"         

def add_funcionario():
               nome = input("Introduza nome: ")
               idade = input("Introduza idade: ")
               sal = input("Introduza salario: ")

               return Funcionario(nome,idade,sal)

def add_Enfermeiro():
               f = add_funcionario()
               a = int(input("Introducir Anos de Experiencia: "))
               
               return Enfermeiro(f, a)

def add_Medico():
               f = add_funcionario()
               Lista_Especialidade = []

               while(True):
                              e = input("Introduza especialidade: ")
                              if e == "":
                                             break 
                              Lista_Especialidade.append(e)

               a = int(input("Introducir Anos de Experiencia: "))

               return Medico(f, Lista_Especialidade, a)

def gravarlista(l):
               e=open('f1.txt','wb')
               pickle.dump(l,e)
               e.close()



def lerlista():
               e=open('f1.txt','rb')
               l = pickle.loads(e.read())
               e.close()

               return l
               

def gravarlistaJson(l):
               with open('f2Json.json', 'w') as f:
                              f.write("[")
                              first = True
                              for x in l:
                                             if first == True:
                                                            first = False
                                             else:
                                                            f.write(",")           
                                             f.write(x.toJSON())
                                             
                              f.write("]")

def lerlistaJson():
               with open('f2Json.json', 'r') as infile:
                              data = json.load( infile)
                              print(data)
               

def ConJSON(l):
               for i in l:
                              print(i.toJSON())

               return l



def main ():
               l = []
               while(True):
                              a = input("Menu:\na.Introduzir Medico\nb.Introduzir enfermeiro\nc.Introduzir funcionario\nd.Ver base de dados\ne.gravar listas\ng.Ler Lista\nh.converter a JSON\n>")

                              if a == "a":
                                             l.append(add_Medico())
                              if a == "b":
                                             l.append(add_Enfermeiro())                              
                              if a == "c":
                                             l.append(add_funcionario())
                              if a == "d":
                                             print(l)
                              if a == "e":
                                             gravarlista(l)
                                             gravarlistaJson(l)
                              if a == "g":
                                             #l = lerlista()
                                             lerlistaJson()

                              if a == "h":
                                             ConJSON(l)


if __name__ == '__main__':
               main()
