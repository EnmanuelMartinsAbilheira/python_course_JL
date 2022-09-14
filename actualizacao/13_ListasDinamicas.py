def main():
               nm = int (input("Quantos nomes quer inserir na lista?: "))
               a = []
               for b in range(nm):
                              a.append(input("Nome (" + str(b+1) + ") : "))
               print(a)

if __name__ == "__main__":
    main()