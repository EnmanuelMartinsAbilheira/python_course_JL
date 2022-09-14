import json

class pessoa:
               def __init__(self,nome,contactos):
                              self.nome = nome  
                              self.contactos = contactos
               
               def __str__(self):
                              return self.nome + " , " + str(self.contactos)

               def toJSON(self):
                              return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
               
def criar_contactos():
               lista = []
               while True:
                              contacto = input("introduza contacto:")
                              if contacto == "":
                                             return lista 
                              lista.append(contacto)
             
def contacto_especifico(arvore,nome):
               lista = []
               for x,y in arvore.items():
                              for c in y.contactos:
                                             if c == nome:
                                                            lista.append(x)
               
               return lista



def gravarlistaJson(arvore):
               with open('f-03ex-Json.json', 'w') as f:
                              f.write("[")
                              first = True
                              for x,y in arvore.items():
                                             if first == True:
                                                            first = False
                                             else:
                                                            f.write(",")           
                                             f.write(y.toJSON())
                                             
                              f.write("]")
        
def lerlistaJson():
               arvore = {}
               with open('f-03ex-Json.json', 'r') as infile:
                              data = json.load( infile)
                              for elem in data:
                                             arvore[elem['nome']] = pessoa(elem['nome'],elem['contactos'])
               return arvore
def main(): 
             arvore = {}
             while(True): 
                             
                             a = input("Menu:\na.adicionar pessoa\nb.listar base de dados \nc.Procurar um contacto em especifico\nd.Gravar arvore em JSON \ne.Leer ficheiro JSON \n >")

                             if a == "a":
                                             nome_pessoa = input("Introducir o seu nome: ")
                                             contactos = criar_contactos()
                                             arvore[nome_pessoa] = pessoa(nome_pessoa,contactos)
                             if a == "b":
                                             for x,y in arvore.items():
                                                            print(x + ":" + str(y))

                             if a == "c":
                                            nome = input("nome da pessoa a procurar: ")
                                            lista = contacto_especifico(arvore,nome)
                                            for x in lista:
                                                           print(x)
                             if a == "d":
                                            gravarlistaJson(arvore)
                              
                             if a == "e":
                                            arvore = lerlistaJson()

                                                            

if __name__ == '__main__':
               main()
