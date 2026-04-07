class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def eje_X(self):
        return self.x

    def eje_Y(self):
        return self.y

    def impresion(self):
        return str(self.x) + "," + str(self.y)
    
    def opuesto(self):
        xaux = self.x*-1
        yaux = self.y*-1
        return Punto(xaux, yaux)

Punto1 = Punto(4, -2)
print(Punto1.eje_X())
print(Punto1.eje_Y())
print(Punto1.impresion())
print(Punto1.opuesto().impresion())