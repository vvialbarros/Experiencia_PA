import random
def adivinar_par_o_impar():
    numero_pc = random.randint(1,2)
    guess = input('Adivina si el numero sera par o impar')

    if guess == 'par' and numero_pc == 2:
        print('Adivinaste, es par!')
    elif guess == 'impar' and numero_pc == 1:
        print('Adivinaste, es impar!')
    else:
        print('No adivinaste.')

    pass
