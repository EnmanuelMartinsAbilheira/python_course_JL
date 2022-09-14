#from classes_24 import Class1, Class2, IInterface
from classes_24 import *


def main():
    c2 = Class2(4,5,6)

    c2.imprime()

    print("c2 instancia de Class1 = " +str(isinstance(c2,Class1)))
    print("c2 instancia de Class2 = " +str(isinstance(c2,Class2)))
    print("c2 Interface de IInterface = " +str(isinstance(c2,IInterface)))
    
if __name__ == "__main__":
    main()