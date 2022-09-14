def main():
    l = []

    while True:
        i = input("Menu:\n\t1. Adicionar\n\t2. Listar\n\t3. Procurar\n\t0. Sair\n>")

        if i == "1":
            l.append((input("Nome: "), input("Morada: "), input("Telefone: ")))
            pass
        elif i == "2":
            for x in l:
                print("Nome: " + x[0] + ", Morada: " + x[1] + ", Telefone: " + x[2])
        elif i == "3":
            nome = input("Nome: ")
            for x in l:
                if x[0] == nome:
                    print("Nome: " + x[0] + ", Morada: " + x[1] + ", Telefone: " + x[2])
        elif i == "0":
            break
        else:
            print("Opcao errada!")


    
if __name__ == "__main__":
    main()
