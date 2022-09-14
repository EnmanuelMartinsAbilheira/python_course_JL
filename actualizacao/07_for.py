def main():

    i = 10
    for b in range(i):    # O ciclo for itera sempre sobre uma lista
        print(b)

    print(type(range(i)))  # Atencao, em Python 2.x o range retorna uma lista.
    print(list(range(i)))  # Em Python 3.x será necessário converter para lista de forma a vermos todos os elementos.

if __name__ == "__main__":
    main()
