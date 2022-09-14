class Carro:
               marca = ""
               idade = 0
               def __init__(self,marca, idade):
                              self.marca = marca
                              self.idade = idade
               
               def __str__(self):
                              return self.marca + " , " + str(self.idade)

class trator(Carro):
               tara_de_reboque = 0
               

               def __init__(self,marca,idade,tara_de_reboque):
                              super().__init__(marca,idade)
                              self.tara_de_reboque = tara_de_reboque

               
               def __str__(self):
                              return super().__str__() + " , " + str(self.tara_de_reboque)

def main():
               l = []
               l.append(Carro("nissa",214))
               l.append(Carro("ford",320))
               l.append(Carro("ferrari",223))
               l.append(Carro("toyota",435))
               l.append(Carro("mini",285))
               
               l.append(trator("nissa",251,1000))

               print(l)
               for k in l:
                              if isinstance(k,trator):
                                             print(k)


if __name__ == '__main__':
               main()