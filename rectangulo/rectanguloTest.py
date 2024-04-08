import unittest


# La clase de prueba
class TestRectangulo(unittest.TestCase):
    # Método de prueba
    def test_suma(self):
        self.assertEqual(2 + 2, 4)

    def test_resta(self):
        self.assertEqual(5 - 3, 2)


if __name__ == '__main__':
    unittest.main()