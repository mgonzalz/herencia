'''
Enunciado: Implementar un programa que calcule la superficie total acristalada de una casa, sabiendo que una 
casa está formada por paredes y que cada pared tiene una orientación (Norte, Oeste, Sur, Este) y posiblemente 
ventanas. Una ventana tiene una superficie que se da como parámetro durante su construcción.
'''
from enum import Enum

# PARTE 1
class Orientacion(Enum): #Lista de las posibles orientaciones de una pared
    NORTE = 'NORTE'
    SUR = 'SUR'
    ESTE = 'ESTE'
    OESTE = 'OESTE'
class Pared:
    def __init__(self, orientacion):
        orientacion = orientacion.upper() #Paso a mayusculas la orientacion
        if orientacion == Orientacion(orientacion).name:
            self.orientacion = orientacion
        else:
            raise ValueError('Orientacion no valida')
        self.ventanas = []
    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)
    def __str__(self):
        return 'Pared: ' + self.orientacion

class Ventana:
    def __init__(self, pared, superficie):
        if isinstance(pared, Pared):
            self.pared = pared
            self.pared.agregar_ventana(self)
        else:
            raise ValueError('La ventana debe estar en una pared')
        self.superficie = superficie

class Casa:
    def __init__(self, paredes):
        if isinstance(paredes, list):
            self.paredes = paredes
        else:
            raise Exception('Una casa debe tener paredes')

    def superficie_acristalada(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie



# Instanciación de las paredes
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

# Instanciación de las ventanas
ventana_norte = Ventana(pared_norte, 0.5) 
ventana_oeste = Ventana(pared_oeste, 1) 
ventana_sur = Ventana(pared_sur, 2) 
ventana_este = Ventana(pared_este, 1) 

# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada())  # Output: 4.5


'''
Enunciado: los edificios modernos tienen a menudo fachadas llamadas "paredes cortina" que actúan como paredes
exteriores al mismo tiempo que son una superficie acristalada transparente. Su código debe poder gestionar 
este nuevo concepto, sabiendo que una pared cortina se define por su orientación y su superficie.
'''

# PARTE 2
class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion) #(self, orientacion)
        Ventana.__init__(self, self, superficie) #(self, pared, superficie) la pared es la misma que la de la clase padre

    def __str__(self):
        return 'Pared cortina: ' + self.orientacion

casa.paredes[2] = ParedCortina("SUR", 10)
print(casa.superficie_acristalada()) # Output: 12.5


'''
Enunciado: se publica una nueva regulación térmica del edificio e impone protecciones externas en las 
ventanas, con el fin de aumentar el aislamiento de las casas residenciales. Su código ahora debe detenerse si 
alguna vez se crea una instancia de una ventana sin protección externa (para eso, use el comando raise 
Exception("mensaje"); este mecanismo se explicará en la sección dedicada a las excepciones). En el contexto 
de este ejercicio, la protección se limitará a una cadena de caracteres ("Persiana", "Estor", etc.).
'''
# PARTE 3: UBICADO EN EL ARCHIVO ejercicio04_parte3.py
