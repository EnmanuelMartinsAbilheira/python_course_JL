

class Class1:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    #decorators: https://www.programiz.com/python-programming/decorator
#    @property
#    def a(self):
#        print("Get a")
#        return self.__a

#    @a.setter
#    def a(self,a):
#        print("Set a")
#        self.__a = a 

    def __str__(self):
        return "string da class 1 com a = " + str(self.a) + " , b= " + str(self.b)

    def __repr__(self):
        return "Representacao da class 1"

    @staticmethod
    def metodo_estatico(a,b):
        return a + b
    
def main():
    l = Class1(2,3)
    l.a = 5
    print(l)
    print([l])

    print("Metodo estatico = " + str(Class1.metodo_estatico(2,3)))

if __name__ == "__main__":
    main()