
def soma(e1,e2):
    return e1 + e2

def subtracao(e1,e2):
    return e1 - e2

def mul(e1,e2):
    return e1 * e2

def div(e1,e2):
    return e1 / e2

def main():
    print("Calculadora")
    while True:
        x = int(input("1º numero: "))
        y = int(input("2º numero: "))
        op = input("Funcao: ")

        if op.lower() == "soma":
            print("Resultado: " + str(soma(x,y)))
        elif op.lower() == "subtracao":
            print("Resultado: " + str(subtracao(x,y)))
        elif op.lower() == "multiplicacao":
            print("Resultado: " + str(mul(x,y)))
        elif op.lower() == "divisao":
            print("Resultado: " + str(div(x,y)))
        else:
            print("Operacao nao reconhecida")


if __name__ == '__main__':
    main()