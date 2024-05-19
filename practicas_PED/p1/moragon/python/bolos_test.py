import unittest
import bolos
class Bolos(unittest.TestCase):
	
	def test_true(self):
		self.assertEqual(1,1)

	def test_rondas_tras_iniciar_partida(self):
		partida = bolos.Partida()

		numero_de_rondas = partida.rondas_restantes
		self.assertEqual(numero_de_rondas,10)

	def test_intentos_para_siguiente_ronda(self):
		partida = bolos.Partida()
		# Pongo un 0, para indicar que no ha tirado ningún bolo, por lo que son 2 intentos.
		partida.tirar_bola(0) 
		partida.tirar_bola(0)

		numero_de_rondas = partida.rondas_restantes
		self.assertEqual(numero_de_rondas, 9)

	def test_intentos_para_siguiente_ronda_con_pleno(self):
		partida = bolos.Partida()

		partida.tirar_bola(10)

		numero_de_rondas = partida.rondas_restantes
		self.assertEqual(numero_de_rondas, 9)

	def test_rondas_tras_jugar_las_10_rondas(self):
		partida = bolos.Partida()
		for i in range(20):
			partida.tirar_bola(0)

		numero_de_rondas = partida.rondas_restantes
		self.assertEqual(numero_de_rondas, 0)
	
	def test_intentamos_jugar_11_rondas(self):
		partida = bolos.Partida()
		for i in range(20):
			partida.tirar_bola(0)

		with self.assertRaises(bolos.PartidaTerminadaException):
			partida.tirar_bola(0)
	
	def test_puntos_partida_simple(self):
		partida = bolos.Partida()
		for i in range(20):
			partida.tirar_bola(0)
		
		self.assertEqual(partida.puntos, 0)

	
		

if __name__ == "__main__":
	unittest.main()