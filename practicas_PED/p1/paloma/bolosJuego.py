registro_rondas = {
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


def tirar_bola(num_bolos_tirados, num_ronda, registro_rondas):
    if not isinstance(num_bolos_tirados, int):
        raise TypeError("El número de bolos tirados debe ser un ENTERO")

    if not isinstance(num_ronda, int):
        raise TypeError("El número de ronda debe ser un entero")

    if num_ronda > 10 or num_ronda < 1:
        raise TypeError(f"El número de ronda debe ser entre 1 y 10, has elejido la ronda {num_ronda}")

    if not isinstance(registro_rondas, dict):
        raise TypeError("el registro de rondas no es un diccionario")

    ronda = registro_rondas[num_ronda]

    if num_ronda != 10 and ronda[0] == 10:
        raise TypeError("Solo puedes tener tiros extras en la ronda 10")


    # Si es la última ronda
    if num_ronda == 10:
        if sum(ronda) == 10:  # Si es el tercer tiro
            ronda.append(num_bolos_tirados)
        if ronda[0] != -1:  # Si es el segundo tiro
            if sum(ronda)+1 == 10 and ronda[0] != 10:
                ronda.append(num_bolos_tirados)
            ronda.append(num_bolos_tirados)

        if ronda[0] == -1:  # Si es el primer tiro
            ronda[0] = num_bolos_tirados

        if ronda[0] + ronda[1] == 10:
            if len(ronda) < 4:
                ronda.append(num_bolos_tirados)


    else:
        if ronda[0] == -1:
            ronda[0] = num_bolos_tirados
        elif ronda[1] == -1:
            ronda[1] = num_bolos_tirados
            if ronda[0] + ronda[1] == 10:
                ronda.append("semipleno")
        else:
            raise TypeError("Solo tienes 2 tiros si no estás en la ronda final")
    return ronda


def calcular_puntos(registro_rondas):
    listaPuntos = []
    for sublist in registro_rondas.values():
        for elemento in sublist:
            if isinstance(elemento, int) and elemento > 0:
                listaPuntos.append(elemento)
            elif isinstance(elemento, str):
                listaPuntos.append(elemento)
    print(f'listaPuntos: {listaPuntos}')

    # Revisar si los dos últimos números son 10
    if len(listaPuntos) > 1:
        # Si un número de la lista es "semipleno", sustitúyelo por la suma num_anterior_semipleno +
        # num_siguiente_al_semipleno
        for i in range(len(listaPuntos)):
            if listaPuntos[i] == "semipleno":
                listaPuntos[i] = listaPuntos[i + 1]
            if listaPuntos[i] == 10:  # pleno
                if i < len(listaPuntos) - 2:
                    listaPuntos[i] = 10 + listaPuntos[i + 1] + listaPuntos[i + 2]
                else:
                    listaPuntos[i] = 10

    return sum(listaPuntos)


