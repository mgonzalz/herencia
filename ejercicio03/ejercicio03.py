'''
Enunciado: en el caso del temido diamante de la herencia múltiple (ver capítulo Conceptos de la POO, sección Herencia múltiple), donde una clase D hereda de dos clases B y C, ambas heredando de una sola clase A, escriba el código que permita, durante la instanciación, inicializar los atributos a, b y c, pertenecientes respectivamente a las clases A, B y C.

'''

class A: 
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c

class B(A):
    def __init__(self, a, b, c): 
        super().__init__(a, b, c)
class C(A):
    def __init__(self, a, b, c): 
        super().__init__(a, b, c)

class D(B, C):
    def __init__(self, a, b, c): 
        super().__init__(a, b, c)


d = D(1, 2, 3) 
print(isinstance(d, A), isinstance(d, B), isinstance(d, C)) #Output: True True True
'''
*isinstance(object, classinfo) se utiliza para determinar si un objeto es una instancia de una clase determinada o de una subclase de ella. Devuelve True o False.
'''
print(d.a, d.b, d.c) #Output: 1 2 3
