class Partida:

    def __init__(self):
        self.rondas_restantes = 10
        self.tiros_restantes = 2
        self.puntos = 0

    
    def tirar_bola(self, numero_bolas):

        if self.rondas_restantes == 0:
            raise PartidaTerminadaException()

        if numero_bolas == 10:
            self.tiros_restantes -= 2 
        else: 
            self.tiros_restantes -= 1

        if self.tiros_restantes == 0: 
            self.rondas_restantes -= 1
            self.tiros_restantes = 2


class PartidaTerminadaException(Exception):
    pass
        