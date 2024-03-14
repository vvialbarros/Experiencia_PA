import random

def juego_del_dado():
    puntaje_jugador=0
    puntaje_compu=0
    input('Presione la tecla Enter')

    while puntaje_jugador<30 and puntaje_compu<30:
        puntaje_jugador+=random.randint(1,6)
        puntaje_compu+=random.randint(1,6)

    if puntaje_jugador>=30 and puntaje_compu>=30:
        print('Empate')
    elif puntaje_jugador>=30 and puntaje_compu<30:
        print('Gano el jugador')
    elif puntaje_compu>=30 and puntaje_jugador<30:
        print('Gano el computador')



    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """

