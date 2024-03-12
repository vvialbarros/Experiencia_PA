from cachipun import cachipun
from adivinar_numero import adivinar_numero
from reaccion_rapida import reaccion_rapida
from suma_rapida import suma_rapida
from memoria import memoria

def menu():
    juegos = {
        '1': cachipun,
        '2': adivinar_numero,
        '3': reaccion_rapida,
        '4': suma_rapida,
        '5': memoria
    }

    while True:
        print("\nMenú de juegos:")
        print("1. Cachipun")
        print("2. Adivinar número")
        print("3. Reacción rápida")
        print("4. Suma rápida")
        print("5. Memoria")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion in juegos:
            print(juegos[opcion]())
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

if __name__ == "__main__":
    menu()