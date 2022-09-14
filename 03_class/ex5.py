
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
               
def main():
               x = Carro("ford",21,3499)
               y = Carro("mercedes",30,4500)
               z = Carro("toyota",30,8787)

               print(x)
               print(y)
               print(z)

if __name__ == '__main__':
               main()