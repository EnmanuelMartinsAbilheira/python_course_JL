
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
    a = Pessoa("Carlos",21)
    b = Pessoa("Filipa",30)
    c = Pessoa("matias",22)
    d = Pessoa("joao",43)
    e = Pessoa("ana",25)
    f = Pessoa("paulo",60)
    lista = []

    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista.append(e)
    lista.append(f)

    lista.append(Carro("ford",1990,1000))
    lista.append(Carro("nissa",1990,1000))
    lista.append(Carro("citroen",1990,1000))
    lista.append(Carro("Mustang",1990,1000))

    print(lista)
    print(len(lista))
    for zz in lista:
                    if isinstance(zz,Pessoa) == True:
                                    print(zz)

    print(lista)
    for k in lista:
                    if isinstance(k,Carro) == True:
                                    print(k)

if __name__ == '__main__':
    main()