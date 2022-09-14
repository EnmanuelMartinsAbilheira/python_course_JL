
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

               print(x.nome)
               print(y.idade)
if __name__ == '__main__':
               main()