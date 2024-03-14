import random
def memoria():
    palabra=''
    contador=0
    while contador<8:
        numero=random.randint(0,9)
        palabra+=str(numero)
        contador+=1
    print('La secuencia a memorizar es',palabra)
    palabra_jugador=str(input('Escriba la secuencia'))
    if palabra_jugador==palabra:
        print('Secuencia correcta, ha ganado el juego')
    else:
        print('Secuencia incorrecta, ha perdido el juego')
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
