
class Carro:
               marca = ""
               ano = 0
               preco = 0
               def __init__(self, marca, ano ,preco):
                              self.marca = marca
                              self.ano = ano
                              self.preco = preco
               
               def __str__(self):
                              return self.marca + " , " + str(self.ano) + " , " + str(self.preco)

class Pessoa:
               nome = ""
               idade = 0
               def __init__(self,nome, idade):
                              self.nome = nome
                              self.idade = idade
               
               def __str__(self):
                              return self.nome + " , " + str(self.idade)
               
def main():
               x = Pessoa("Carlos",21)
               y = Pessoa("Filipa",30)
               lista = []

               lista.append(x)
               lista.append(y)
               lista.append(Carro("seat",1990,1000))

               print(lista)
               for k in lista:
                              if isinstance(k,Carro) == True:
                                             print(k)

if __name__ == '__main__':
               main()