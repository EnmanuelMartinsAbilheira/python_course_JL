def main():
    l =[
        ("Joao", 20,"professor"),
        ("Carlos",30, "engenheiro"),
        ("joana",30, "diretora"),
    ]

    print(l)

    for x in l:
        print(str(x[0]) + " , idade = " + str(x[1]) + " , profissao = " + str(x[2]))
    
    l.append(("antonio",44,"professor"))

    print(l)

    
if __name__ == "__main__":
    main()
