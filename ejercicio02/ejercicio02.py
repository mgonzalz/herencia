class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb"
        super().B()
        print(self.b)
 
base = Base() # Instancia de la clase base
derivada = Derivada() # Instancia de la clase derivada

base.A() # Output: a. LLama al método A de la clase base.

derivada.A() # Output: a. No sale aa debido a que en el __init__ de la clase derivada se sobreescribe el valor de a.

print()

base.B() # Output: b. LLama al método B de la clase base.

derivada.B()

'''
Output: bb
        bb
Se llama al método B de la clase base, pero se sobreescribe el valor de b en el método B de la clase derivada.
Dentro del método B de la clase derivada se llama al método B de la clase base y se imprime el valor de b. Por eso se repite dos veces.
'''

base.C() #Output: c. LLama al método C de la clase base.

derivada.C() #Output: cc. LLama al método C que es heredado de base.

derivada = base #Se iguala la instancia base a la variable derivada. Ahora derivada es una instancia de la clase base.

derivada.C() #Output: c. Se llama al método C de la clase base.
