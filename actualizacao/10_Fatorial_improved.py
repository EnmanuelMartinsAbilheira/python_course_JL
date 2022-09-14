def fatorial(a:int): #especificacao do tipo de entrada (normalmente nao e utilizado)
            res = 1
            iter = 0
            for b in range(a):
                        res = res * (b+1)
                        iter = iter + 1
            return [res, iter]

def main():
               a = int(input("introduza valor: "))
               print("Resultado = " + str(fatorial(a)[0]) + " em Iteracoes = " + str(fatorial(a)[1])) #Atencao ao tipo de retorno da funcao fatorial


if __name__ == '__main__':
               main()