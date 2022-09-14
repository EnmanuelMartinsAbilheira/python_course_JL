import json



def add_novo_valor_lista(lista):
               chave = input("introducir nova chave: ")
               valor = input("introducir valor: ")
               lista[chave] = valor

def GuardarEnJson(lista):
               with open('n.json', 'w') as f:
                              json.dump(lista,f,indent=4)
def main():
               try:
                              with open('n.json', 'r') as file:
                                             lista = json.load(file)
               except:
                              lista = {}
                              pass


               while(True):
                              a = input("Menu:\na.Introduzir novo valor na lista\nb.Guardar novos valores\nc.leer lista\nd.Guardar json\n>")

                              if a == "a":
                                             add_novo_valor_lista(lista)
                              if a == "b":
                                             pass
                              if a  == "c":
                                             print(lista)
                              if a == "d":
                                             GuardarEnJson(lista)

                              


if __name__ == '__main__':
               main()
