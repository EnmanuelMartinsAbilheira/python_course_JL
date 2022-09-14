def main():
    t = ("Joao", "Carlos", "Joaquim",44,55.4)
    print(t)

    for x in t:
        print(x)

    #Remover primeiro elemento tuplo
    #t.append("asd")
    k = t[1:]
    print(t)
    print(k)

    p = ("Antonio","Joana") + t
    print(p)
    
if __name__ == "__main__":
    main()
