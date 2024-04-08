import unittest
import rectangulo
from rectangulo import Rectangulo, obtener_x_y, calcular_area, calcular_perimetro, calcular_centro
from rectangulo import obtener_diagonal, seSuperponen
"""
    Capaz de calcular su área
    Capaz de calcular su perímetro
    Capaz de calcular su centro
    Capaz de calcular su diagonal
    Capaz de comprobar si se superpone con otro rectángulo (defina el criterio de superposición)
    """
class TestRectangulo(unittest.TestCase):

    def test_calcular_area(self):
        r = Rectangulo(2,4,4,7)
        x,y= obtener_x_y(r.xmin, r.xmax, r.ymin, r.ymax)
        area = calcular_area(x,y)
        self.assertEqual(area, 6)

    def test_calcular_perimetro(self):
        r = Rectangulo(2, 4, 4, 7)
        x, y = obtener_x_y(r.xmin, r.xmax, r.ymin, r.ymax)
        perimetro = calcular_perimetro(x, y)
        self.assertEqual(perimetro, 2+2+3+3)

    def test_calcular_centro(self):
        # la mitad de x y la mitad de y
        r = Rectangulo(1, 4, 2, 6)
        x_centro, y_centro = calcular_centro(r.xmin, r.xmax, r.ymin, r.ymax)
        self.assertEqual(x_centro, 2.5)
        self.assertEqual(y_centro, 4.0)

    def test_calcular_diagonal(self):
        r = Rectangulo(1, 4, 2, 6)
        x_diagonal, y_diagonal = obtener_diagonal(r)
        self.assertEqual(x_diagonal, 1)
        self.assertEqual(y_diagonal, 6)

    def test_superposicion(self):
        r1 = Rectangulo(1,4,1,6)
        r2 = Rectangulo(3,5,6,7)
        self.assertEqual(seSuperponen(r1,r2))


if __name__ == '__main__':
    unittest.main()