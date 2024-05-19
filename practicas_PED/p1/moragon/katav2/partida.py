import re

def calcular_resultado(bolos):
    __la_entrada_tiene_sentido__(bolos)
    __es_el_numero_de_rondas_correcto__(bolos)
    resultado = 0
    extra = 0
    plus = 0
    for bolo in bolos:
        
        if bolo == 'X':
            bolo = 10
            plus = 2
        
        if bolo == '&':
            bolo = 10
            plus = 1

        if extra > 0:
            if extra > 2:
                resultado += int(bolo)
                extra -= 1
            resultado += int(bolo)
            extra -=1

        resultado += int(bolo)

        if bolo == 10:
            extra += plus

    
    return resultado

def __la_entrada_tiene_sentido__(bolos):
    pattern = re.compile(r'[^0-9&X]')
    coincidencia = pattern.search(bolos)
    if coincidencia:
        raise EntradaSinSentidoException()

def __es_el_numero_de_rondas_correcto__(bolos):
    position = 0
    for bolo in bolos:
        if bolo == "X" or bolo == "&":
            position += 2
        else:
            position +=1

        if (bolo == "X" or bolo == "&") and position == 20:
            break

    
    if position != 20:
        raise NumeroDeRondasIrregularException()
    
    

class NumeroDeRondasIrregularException(Exception):
    pass

class EntradaSinSentidoException(Exception):
    pass