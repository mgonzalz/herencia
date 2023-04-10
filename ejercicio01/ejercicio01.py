#PARTE 1
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def traslacion(self, a, b):
        self.x += a
        self.y += b
    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)

a = Punto2D(1, 2)
print("A = {}".format(a)) #Output: A = X: 1; Y: 2
a.traslacion(-1, -2)
print("A = {}".format(a)) #Output: A = X: 0; Y: 0
b = Punto2D(-3, 0)
b.traslacion(5, -1)
print("B = {}".format(b)) #Output: B = X: 2; Y: -1


#PARTE 2

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def traslacion(self, a, b, c):
        super().traslacion(a, b)
        self.z += c
    def __str__(self):
        return super().__str__() + "; Z = {}".format(self.z)

c = Punto3D(1,5,-3)
c.traslacion(0, -2, 1)
print("C = {}".format(c)) #Output: C = X: 1; Y: 3; Z = -2
