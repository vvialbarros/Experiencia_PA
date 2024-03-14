import random
def cachipun():

    numero = random.randint(1, 3)
    usuario = input('Elije piedra, papel o tijera \n')
    opcion_pc = ''
    if numero == 3 and usuario == 'tijera' or numero == 1 and usuario == 'piedra' or numero == 2 and usuario == 'papel':
        print('Empate')
    elif numero == 3 and usuario == 'piedra' or numero == 1 and usuario == 'papel' or numero == 2 and usuario == 'tijera':
        print('Ganaste!')
    else:
        print('Perdiste')

    pass