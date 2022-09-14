import os.path
from os import path
import json


def ler_json(ficheiro):
    if path.exists(ficheiro) == False:
        return {}

    with open(ficheiro, encoding = "utf8") as f:
        return json.load(f)
    return {}

def gravar_json(d,ficheiro):
    with open(ficheiro, 'w',encoding = "utf8") as f:
        json.dump(d,f,indent=4)

def main():
    d = ler_json('db.json')

    while True:
        i = input("Menu:\n\t1. Adicionar\n\t2. Listar\n\t3. Procurar\n\t4. Remover\n\t0. Sair\n>")

        if i == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            Morada = input("Morada: ")

            d[telefone] = {"Nome" : nome, "Telefone": telefone, "Morada" : Morada}
            pass

        elif i == "2":
            for key,value in d.items():
                print(value["Nome"] + " , " + value["Morada"] + " , " + value["Telefone"])

        elif i == "3":
            telefone = input("Telefone: ")
            if telefone in d:
                print(d.get(telefone)["Nome"] + " , " + d.get(telefone)["Morada"] + " , " + d.get(telefone)["Telefone"])
            else:
                print("Nao encontrado!")

        elif i == "4":
            telefone = input("Telefone: ")
            if telefone in d: #Em python 2.x seria d.has_key(telefone)
                del d[telefone]


        elif i == "0":
            break
            
        else:
            print("Opcao errada!")

        gravar_json(d,'db.json')
    
if __name__ == "__main__":
    main()
