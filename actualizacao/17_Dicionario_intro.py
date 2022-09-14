#import json
from json import dumps


def main():
    dic = {
                "joao" : 10,
                "Emanuel" : 15,
                "Carlos" : {
                    "idade" : 20,
                    "professor": {
                                    "escola" : "Lisboa",
                                    "escolaridade": [8,9,10]
                    }
                }
    }

    print(len(dic))
    print(dic.get("Carlos").get("professor"))
    print(dic.get("joao"))
    print(dic.keys())

    #dic["antonio"] = 30

    #print(dic)

    #del dic["Carlos"]

    #print(dic)

    #exportar dicionario para JSON (Validar em https://jsonformatter.curiousconcept.com/#)
    #print(dumps(dic,indent=4))

    #for key,value in dic.items():
    #    print(value)
if __name__ == "__main__":
    main()