import unittest
import partida

class Katav2(unittest.TestCase):
    def test_mi_primer_test(self):
        bolos = "0" * 20
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 0)
    
    def test_mi_segundo_test(self):
        bolos = "00000000000000000001"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 1)

    def test_mi_tercer_test(self):
        bolos = "00000000000000090001"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10)
    # /Cambio de / -> X
    def test_partida_con_un_strike(self):
        bolos = "X23" + "0"*16
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado,20)
    
    def test_partida_con_dos_strikes(self):
        bolos = "XX45" + "0"*14
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, (10 + 10 + 4) + (10 + 4 + 5) + 4 + 5)
    
    def test_partida_con_tres_strikes(self):
        bolos = "XXX72" + "0"*12
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10 + 10 + 10 + 10 + 10 + 7 + 10 + 7 + 2 + 7 + 2)
    
    def test_partida_casi_todo_strikes(self):
        bolos = "X"*9 + "45"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, (10 + 10 + 10)*7 + 10 + 10 + 4 + 10 + 4 + 5 + 4 + 5)

    # Supongo que las bolas extras cuentan como bolas normales y no se cuentan solo en el bonus
    def test_partida_strike_en_el_ultimo_tiro(self):
        bolos = "0"*18 + "X34"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10 + 3 + 4 + 3 + 4)

    def test_partida_con_un_spare(self):
        bolos = "&40" + "0"*16
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10 + 4 + 4)

    def test_partida_con_dos_spare(self):
        bolos = "&&40" + "0"*14
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10 + 10 + 10 + 4 + 4)    
    
    def test_partida_con_casi_todo_spare(self):
        bolos = "&&&&&&&&&10" #&"*9 + "10"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, (10 + 10)*8 + 10 + 1 + 1)   

    # Supongo que las bolas extras cuentan como bolas normales y no se cuentan solo en el bonus
    def test_partida_con_casi_todo_spare(self):
        bolos = "0"*18 + "&5"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10 + 5 + 5)   

    def test_una_partida_de_mas_de_10_rondas_sin_extras(self):
        bolos = "0"*21
        with self.assertRaises(partida.NumeroDeRondasIrregularException):
            partida.calcular_resultado(bolos)

    def test_una_partida_de_menos_de_10_rondas(self):
        bolos = "0"*19
        with self.assertRaises(partida.NumeroDeRondasIrregularException):
            partida.calcular_resultado(bolos)

    def test_mono_loco(self):
        bolos = "ksaj34@fñlkajsdflañksdf"
        with self.assertRaises(partida.EntradaSinSentidoException):
            partida.calcular_resultado(bolos)

    def partida_normal(self):
        bolos = "5318X&00XX&&XX"
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, ) 
    
    # Cambio de diseño
    def partida_con_un_spare_nuevo(self):
        bolos = "3&42" + "0"*16
        resultado = partida.calcular_resultado(bolos)

        self.assertEqual(resultado, 10 + 4 + 4 + 2)

# Spare solo se puede en la segunda tirada

if __name__ == "__main__":
    unittest.main()