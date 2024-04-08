import unittest
import rectangulo
from rectangulo import Rectangulo, obtener_x_y, calcular_area, calcular_perimetro


# La clase de prueba
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


if __name__ == '__main__':
    unittest.main()