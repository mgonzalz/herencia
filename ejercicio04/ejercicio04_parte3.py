
'''
Enunciado: se publica una nueva regulación térmica del edificio e impone protecciones externas en las 
ventanas, con el fin de aumentar el aislamiento de las casas residenciales. Su código ahora debe detenerse 
si alguna vez se crea una instancia de una ventana sin protección externa (para eso, use el comando raise 
Exception("mensaje"); este mecanismo se explicará en la sección dedicada a las excepciones). En el 
contexto de este ejercicio, la protección se limitará a una cadena de caracteres ("Persiana", "Estor", 
etc.).
'''
from enum import Enum
class Orientacion(Enum):
    NORTE = 'NORTE'
    SUR = 'SUR'
    ESTE = 'ESTE'
    OESTE = 'OESTE'

class Proteccion(Enum): #Lista de las posibles protecciones de una ventana: PARTE 3 DEL EJERCICIO
    PERSIANA = 'PERSIANA'
    ESTOR = 'ESTOR'
    CORTINA = 'CORTINA'

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
    def __init__(self, pared, superficie, proteccion): #PARTE 3 DEL EJERCICIO: AÑADIDO PROTECCION
        if isinstance(pared, Pared):
            self.pared = pared
            self.pared.agregar_ventana(self)
        else:
            raise ValueError('La ventana debe estar en una pared')
        if isinstance(proteccion, str):
            if proteccion.upper() == Proteccion(proteccion.upper()).name and proteccion != None:
                self.proteccion = proteccion
            else:
                raise Exception('Protección no valida')
        else:
            raise Exception('Protección obligatoria')
        self.superficie = superficie

class Casa:
    def __init__(self, paredes):
        if isinstance(paredes, list):
            self.paredes = paredes
        else:
            raise Exception('Protección obligatoria')

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
ventana_norte = Ventana(pared_norte, 0.5) # Output: TypeError: __init__() missing 1 required positional argument:'proteccion'
ventana_norte = Ventana(pared_norte, 0.5, None) #Output: Exception: Protección obligatoria
ventana_norte = Ventana(pared_norte, 0.5, "Persiana") 
ventana_oeste = Ventana(pared_oeste, 1, "Estor")
ventana_sur = Ventana(pared_sur, 2, "Cortina") 
ventana_este = Ventana(pared_este, 1, "Persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada()) #4,5

