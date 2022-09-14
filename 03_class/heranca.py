class Pessoa:
               nome = ""
               idade = 0
               def __init__(self,nome, idade):
                              self.nome = nome
                              self.idade = idade
               
               def __str__(self):
                              return self.nome + " , " + str(self.idade)

class aluno(Pessoa):
               n_aluno = 0
               curso = ""

               def __init__(self,nome,idade,n_aluno,curso):
                              super().__init__(nome,idade)
                              self.n_aluno = n_aluno
                              self.curso = curso
               
               def __str__(self):
                              return super().__str__() + " , " + str(self.n_aluno) + " , " + self.curso

def main():
               l = []
               l.append(Pessoa("Carlos",21))
               l.append(Pessoa("Filipa",30))
               l.append(Pessoa("matias",22))
               l.append(Pessoa("joao",43))
               l.append(Pessoa("ana",25))
               
               l.append(aluno("joao",21,1,"eletronica"))

               print(l)
               for k in l:
                              if isinstance(k,aluno):
                                             print(k)


if __name__ == '__main__':
               main()