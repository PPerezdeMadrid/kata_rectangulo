import unittest


# La clase de prueba
class TestRectangulo(unittest.TestCase):

    def calcular_area(self):
        r = Rectangulo(2,4,4,7)
        x,y= r.obtener_x_y()
        area = r.calcular_area()
        self.assertEqual(area, 6)

    def test_resta(self):
        self.assertEqual(5 - 3, 2)


if __name__ == '__main__':
    unittest.main()