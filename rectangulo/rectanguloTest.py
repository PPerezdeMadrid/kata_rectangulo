import unittest
import rectangulo
from rectangulo import Rectangulo, obtener_x_y, calcular_area, calcular_perimetro, calcular_centro
from rectangulo import obtener_diagonal, r1SeSuperponeAr2
"""
    Capaz de calcular su área
    Capaz de calcular su perímetro
    Capaz de calcular su centro
    Capaz de calcular su diagonal
    Capaz de comprobar si se superpone con otro rectángulo (defina el criterio de superposición)
    """
class TestRectangulo(unittest.TestCase):
    def test_xmax_menor_que_xmin(self):
        with self.assertRaises(ValueError):
            Rectangulo(4, 1, 1, 6)

    def test_ymax_menor_que_ymin(self):
        with self.assertRaises(ValueError):
            Rectangulo(1, 4, 6, 3)
    def test_calcular_area(self):
        r = Rectangulo(2,4,4,7)
        x,y= obtener_x_y(r.xmin, r.xmax, r.ymin, r.ymax)
        area = calcular_area(x,y)
        self.assertEqual(area, 6)

    def test_calcular_area_con_numeros_negativos(self):
        r = Rectangulo(-1, 1, -2, 2)
        # area de 2 x 4
        x, y = obtener_x_y(r.xmin, r.xmax, r.ymin, r.ymax)
        area = calcular_area(x, y)
        self.assertEqual(area, 2*4)


    def test_calcular_perimetro(self):
        r = Rectangulo(2, 4, 4, 7)
        x, y = obtener_x_y(r.xmin, r.xmax, r.ymin, r.ymax)
        perimetro = calcular_perimetro(x, y)
        self.assertEqual(perimetro, 2+2+3+3)

    def test_calcular_perimetro_con_numeros_negativos(self):
        r = Rectangulo(-1, 1, -2, 2)
        # area de 2*2 + 4*2
        x, y = obtener_x_y(r.xmin, r.xmax, r.ymin, r.ymax)
        perimetro = calcular_perimetro(x, y)
        self.assertEqual(perimetro, 2*2 + 4*2)

    def test_calcular_centro(self):
        # la mitad de x y la mitad de y
        r = Rectangulo(1, 4, 2, 6)
        x_centro, y_centro = calcular_centro(r.xmin, r.xmax, r.ymin, r.ymax)
        self.assertEqual(x_centro, 2.5)
        self.assertEqual(y_centro, 4.0)

    def test_calcular_centro_num_negativo(self):
        r = Rectangulo(-1, 1, -1, 1)
        x_centro, y_centro = calcular_centro(r.xmin, r.xmax, r.ymin, r.ymax)
        self.assertEqual(x_centro, 0.0)
        self.assertEqual(y_centro, 0.0)

    def test_calcular_diagonal(self):
        r = Rectangulo(1, 4, 2, 6)
        x_diagonal, y_diagonal = obtener_diagonal(r)
        self.assertEqual(x_diagonal, 1)
        self.assertEqual(y_diagonal, 6)

    def test_calcular_diagonal_num_negativos(self):
        r = Rectangulo(-2, 2, -2, 6)
        x_diagonal, y_diagonal = obtener_diagonal(r)
        self.assertEqual(x_diagonal, -2)
        self.assertEqual(y_diagonal, 6)


    def test_superposicion(self):
        r1 = Rectangulo(1,4,1,6)
        r2 = Rectangulo(3,5,6,7)
        self.assertTrue(r1SeSuperponeAr2(r1,r2))

    def test_no_se_superponen(self):
        r1 = Rectangulo(1, 4, 1, 6)
        r2 = Rectangulo(4.5, 6, 7, 8.5)
        self.assertFalse(r1SeSuperponeAr2(r1, r2))

    def test_superposicion_mismo_lado(self):
        r1 = Rectangulo(1, 4, 1, 6)
        r2 = Rectangulo(4, 10, 1, 6)
        self.assertTrue(r1SeSuperponeAr2(r1, r2))


if __name__ == '__main__':
    unittest.main()