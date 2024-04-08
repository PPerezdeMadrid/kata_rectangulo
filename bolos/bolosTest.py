import unittest
import bolosJuego
from bolosJuego import tirar_bola, calcular_puntos

"""
Un jugador juega 10 rondas, vamos a tener un contador
"""


class TestdeBolos(unittest.TestCase):
    def setUp(self):
        self.registro_rondas = {
            1: [-1, -1],
            2: [-1, -1],
            3: [-1, -1],
            4: [-1, -1],
            5: [-1, -1],
            6: [-1, -1],
            7: [-1, -1],
            8: [-1, -1],
            9: [-1, -1],
            10: [-1, -1]
        }

    def test_juega_una_ronda(self):
        tirar_bola(0, 1, self.registro_rondas)  # tiro 0 en la ronda 1
        tirar_bola(0, 1, self.registro_rondas)  # tiro 0 en la ronda 1
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, 0)

    def test_juego_10_rondas_tiro_1_bolo(self):
        for i in range(1, 11):
            tirar_bola(1, i, self.registro_rondas)
            tirar_bola(1, i, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, 20)

    def test_hago_pleno_en_la_ronda_1_en_el_resto_tiro_un_bolo_por_bola(self):

        tirar_bola(10, 1, self.registro_rondas)
        for i in range(2, 11):
            tirar_bola(1, i, self.registro_rondas)
            tirar_bola(1, i, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, 30)

    def test_hago_mas_de_un_pleno(self):
        tirar_bola(10, 1, self.registro_rondas)
        tirar_bola(10, 2, self.registro_rondas)
        for i in range(3, 11):
            tirar_bola(1, i, self.registro_rondas)
            tirar_bola(3, i, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, (10 + 10 + 1) + (10 + 1 + 3) + ((1 + 3) * 8))

    def test_hago_un_semipleno(self):
        tirar_bola(5, 1, self.registro_rondas)
        tirar_bola(5, 1, self.registro_rondas)
        for i in range(2, 11):
            tirar_bola(1, i, self.registro_rondas)
            tirar_bola(1, i, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos,
                         (5 + 5 + 1) + (1 + 1) + (1 + 1) + (1 + 1) + (1 + 1) + (1 + 1) + (1 + 1) + (1 + 1) + (1 + 1) + (
                                 1 + 1))

    # Tras la última ronda, si es necesario, se lanzan una o dos bolas extra para anotar el bonus final.
    # Suponemos que si saca semipleno en la ronda 10, tiene derecho a un tiro extra
    # Suponemos que si saca pleno en la ronda 10, tiene derecho a dos tiros extra

    def test_hago_un_semipleno_en_la_ronda_10(self):
        for i in range(1, 10):
            tirar_bola(1, i, self.registro_rondas)
            tirar_bola(1, i, self.registro_rondas)
        tirar_bola(5, 10, self.registro_rondas)
        tirar_bola(5, 10, self.registro_rondas)
        tirar_bola(2, 10, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, (1 + 1) * 9 + (5 + 5 + 2) + 2)

    def test_hago_pleno_en_la_ronda_10(self):
        for i in range(1, 10):
            tirar_bola(1, i, self.registro_rondas)
            tirar_bola(1, i, self.registro_rondas)
        tirar_bola(10, 10, self.registro_rondas)
        tirar_bola(10, 10, self.registro_rondas)
        tirar_bola(10, 10, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        # [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10]
        # [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 30, 10, 10]
        self.assertEqual(puntos, (1 + 1) * 9 + (10 + 10 + 10) + 10 + 10)

    # No queda claro cual es el resultado
    # si un jugador hace dos plenos seguidos, supondremos que el resultado en ese instante será (10+10)
    # --> Puntos: todavía no lo sé
    # Mi diseño permite partidas incompletas

    def test_puntos_en_dos_rondas_con_pleno(self):
        tirar_bola(10, 1, self.registro_rondas)
        tirar_bola(10, 2, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)  # Calcular_puntos_parciales
        self.assertEqual(puntos, (10 + 10))  # Partida Incompleta

    def test_puntos_en_5_rondas_con_pleno(self):
        for i in range(1, 6):
            tirar_bola(10, i, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, (10 + 10 + 10) + (10 + 10 + 10) + (10 + 10 + 10) + 10 + 10)

    def test_tirar_strings_como_numero_de_bolos(self):
        with self.assertRaises(TypeError):
            tirar_bola("Paloma", 1, self.registro_rondas)

    def test_tirar_strings_como_numero_de_ronda(self):
        with self.assertRaises(TypeError):
            tirar_bola(1, "ronda 10", self.registro_rondas)

    def test_registrar_las_rondas_sin_un_diccionario(self):
        with self.assertRaises(TypeError):
            tirar_bola(1, 10, "rondas: 1(22)")

    def test_tirar_ronda_mayor_a_10(self):
        with self.assertRaises(TypeError):
            tirar_bola(1, 11, self.registro_rondas)

    def test_tirar_ronda_menor_a_1(self):
        with self.assertRaises(TypeError):
            tirar_bola(1, 0, self.registro_rondas)

    def test_tiras_tres_bolos_en_la_ronda_1(self):
        with self.assertRaises(TypeError):
            tirar_bola(1, 1, self.registro_rondas)
            tirar_bola(1, 1, self.registro_rondas)
            tirar_bola(1, 1, self.registro_rondas)

    def test_hago_un_pleno_no_puedo_volver_a_tirar(self):
        with self.assertRaises(TypeError):
            tirar_bola(10, 1, self.registro_rondas)
            tirar_bola(10, 1, self.registro_rondas)

    def test_ronda_perfecta(self):
        for i in range(1, 11):
            tirar_bola(10, i, self.registro_rondas)
        tirar_bola(10, 10, self.registro_rondas)
        tirar_bola(10, 10, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, 320)
        # [30,30,30,30,30,30,30,30,30,30, 10, 10] = 320

    def test_ronda_perfecta_menos_bolas_extras(self):
        for i in range(1, 11):
            tirar_bola(10, i, self.registro_rondas)
        tirar_bola(2, 10, self.registro_rondas)
        tirar_bola(5, 10, self.registro_rondas)
        puntos = calcular_puntos(self.registro_rondas)
        self.assertEqual(puntos, 286)
        # [10,-1,10,-1,10,-1,10,-1,10,-1,10,-1,10,-1,10,-1,10,2,5] =
        # [30,30,30,30,30,30,30,30,22,17,2,5]

    """ Comentarios Raúl: ¿Que test aportan realmente al diseño?
    # No quedan más rondas (hecho)
    # tirar bolos --> mal tipo de datos (hecho)
    # Test ronda perfecta --> ronda extra (hecho)
    # Test ronda perfecta menos los últimos tiros
    # Tres bolas en una ronda (hecho)
    # Partida no terminada
    """


if __name__ == '__main__':
    unittest.main()
