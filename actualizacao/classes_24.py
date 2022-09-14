class Class1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "string da class 1 com a = " + str(self.a) + " , b= " + str(self.b)

    def metodo1(self,x):
        print("Metodo 1 da Class 1")
        self.a = x + self.a

    def __repr__(self):
        return "Representacao da class 1"

class IInterface:
    def imprime(self):
        raise NotImplementedError

class Class2(Class1,IInterface):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c

    def imprime(self):
        print("Interface Implementada")