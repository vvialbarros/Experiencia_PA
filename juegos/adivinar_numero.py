import random
def adivinar_numero():
    numero_generado = random.randint(1,10)
    jugador = int(input('Adivina un numero del 1 al 10 \n'))
    if jugador == numero_generado:
        print('Adivinaste!')
    else:
        print('No adivinaste.')
    
    pass
