

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

class Class2(Class1):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c

#    def metodo1(self,x):
#        print("Metodo 1 da Class 2")
#        self.a = x + self.a
    
def main():
    c1 = Class1(2,3)
    c2 = Class2(4,5,6)

    c2.metodo1(5)

    print(c2)
    
    print("c1 instancia de Class1 = " + str(isinstance(c1,Class1)))
    print("c1 instancia de Class2 = " +str(isinstance(c1,Class2)))
    print("c2 instancia de Class1 = " +str(isinstance(c2,Class1)))
    print("c2 instancia de Class2 = " +str(isinstance(c2,Class2)))
    
if __name__ == "__main__":
    main()