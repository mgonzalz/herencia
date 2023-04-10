# Herencia: Entrega por Grupos de Trabajo: UML Y CÓDIGO

Link: https://github.com/mgonzalz/herencia.git

**a. Herencia "simple"**


Enunciado: definir una clase Punto2D que tenga dos atributos x e y, y que implemente un método de traslacion() que reciba como parámetro las dos componentes horizontal y vertical de la traslación, y modifique las coordenadas del punto en cuestión según el principio de que una traslación (a, b) consiste en sumar a (respectivamente b), al componente x (respectivamente y) de un punto.


Comportamiento esperado:


a = Punto2D(1, 2) 

print("A = {}".format(a)) 

->->-> A = X: 1; Y: 2 

a.traslacion(-1, -2) 

print("A = {}".format(a)) 

->->-> A = X: 0; Y: 0 

b = Punto2D(-3, 0) 

b.traslacion(5, -1) 

print("B = {}".format(b)) 

->->-> B = X: 2; Y: -1 

Enunciado: ahora añada la gestión de un punto en tres dimensiones, según los mismos principios que el punto 2D. Nota: esta adición se debe realizar sin acceder directamente a los componentes x e y del punto 3D.

Comportamiento esperado:

c = Punto3D(1,5,-3) 

c.traslacion(0, -2, 1) 

print("C = {}".format(c)) 

->->-> C = X: 1; Y: 3; Z = -2 


**b. Puzzle**


Enunciado: ¿qué muestra este programa en la salida estándar?

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
 
base = Base() 

derivada = Derivada() 
 
base.A() 

derivada.A() 

print() 

base.B() 

derivada.B() 

base.C() 

derivada.C() 

derivada = base 

derivada.C() 


**c. Herencia múltiple - Diamante y argumentos de constructor**


Enunciado: en el caso del temido diamante de la herencia múltiple (ver capítulo Conceptos de la POO, sección Herencia múltiple), donde una clase D hereda de dos clases B y C, ambas heredando de una sola clase A, escriba el código que permita, durante la instanciación, inicializar los atributos a, b y c, pertenecientes respectivamente a las clases A, B y C.


Comportamiento esperado:


d = D(1, 2, 3) 

print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
->->-> True True True 

print(d.a, d.b, d.c) 

->->-> 1 2 3 


**d. Herencia múltiple - Caso "real"**


Enunciado: Implementar un programa que calcule la superficie total acristalada de una casa, sabiendo que una casa está formada por paredes y que cada pared tiene una orientación (Norte, Oeste, Sur, Este) y posiblemente ventanas. Una ventana tiene una superficie que se da como parámetro durante su construcción.


Comportamiento esperado:


Instanciación de las paredes 

pared_norte = Pared("NORTE") 

pared_oeste = Pared("OESTE") 

pared_sur = Pared("SUR") 

pared_este = Pared("ESTE") 


Instanciación de las ventanas 

ventana_norte = Ventana(pared_norte, 0.5) 

ventana_oeste = Ventana(pared_oeste, 1) 

ventana_sur = Ventana(pared_sur, 2) 

ventana_este = Ventana(pared_este, 1) 


Instanciación de la casa con las 4 paredes 

casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 

print(casa.superficie_acristalada()) 

->->-> 4.5 # 0.5 + 1 + 2 + 1 


Enunciado: los edificios modernos tienen a menudo fachadas llamadas "paredes cortina" que actúan como paredes exteriores al mismo tiempo que son una superficie acristalada transparente. Su código debe poder gestionar este nuevo concepto, sabiendo que una pared cortina se define por su orientación y su superficie.


Comportamiento esperado:


casa.paredes[2] = ParedCortina("SUR", 10) 

print(casa.superficie_acristalada()) 

->->-> 12.5 

Enunciado: se publica una nueva regulación térmica del edificio e impone protecciones externas en las ventanas, con el fin de aumentar el aislamiento de las casas residenciales. Su código ahora debe detenerse si alguna vez se crea una instancia de una ventana sin protección externa (para eso, use el comando raise Exception("mensaje"); este mecanismo se explicará en la sección dedicada a las excepciones). En el contexto de este ejercicio, la protección se limitará a una cadena de caracteres ("Persiana", "Estor", etc.).


Comportamiento esperado:


ventana_norte = Ventana(pared_norte, 0.5) 

->->-> TypeError: __init__() missing 1 required positional argument: 

'proteccion' 

ventana_norte = Ventana(pared_norte, 0.5, None) 

->->-> Exception: Protección obligatoria 

ventana_norte = Ventana(pared_norte, 0.5, "Persiana") 

[...] 

print(casa.superficie_acristalada()) 

->->-> 4.5 
