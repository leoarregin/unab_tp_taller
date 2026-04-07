from Ejercicio2 import Punto

class Linea:
    def __init__(self, _punto_a: Punto, _punto_b: Punto):
        self._punto_a = _punto_a
        self._punto_b = _punto_b

    def show(self):
        return self._punto_a.impresion() + ", " + self._punto_b.impresion()

    def mueve_derecha(self, n):
        self._punto_a.x += n
        self._punto_b.x += n

    def mueve_izquierda(self, n):
        self._punto_a.x -= n
        self._punto_b.x -= n

    def mueve_arriba(self, n):
        self._punto_a.y += n
        self._punto_b.y += n

    def mueve_abajo(self, n):
        self._punto_a.y -= n
        self._punto_b.y -= n

p1 = Punto(3, 4)
p2 = Punto(5, 6)
linea1 = Linea(p1, p2)

print(linea1.show())