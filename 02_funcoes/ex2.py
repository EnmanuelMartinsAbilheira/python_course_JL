def fatorial(a):
               res = 1
               for b in range(a):
                              res = res * (b+1)
               return res

def main():
               a = int(input("introduza valor: "))
               print("Resultado = " + str(fatorial(a)) )


if __name__ == '__main__':
               main()