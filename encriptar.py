
def encriptar_mensaje(mensaje: str) -> str:
    """
    Esta función toma un mensaje como entrada y lo encripta utilizando un libro_super_secreto.txt. 
    Cada letra del mensaje se busca en el libro y se transforma en un string con la siguiente estructura:
    
    "numero_linea,numero_palabra,numero_letra_en_palabra"
    
    Donde:
    - numero_linea es la línea en la que se encuentra la letra en el libro.
    - numero_palabra es la palabra en la que se encuentra la letra en la línea.
    - numero_letra_en_palabra es la posición de la letra en la palabra.
    
    Luego se concatenan todos los strings de cada letra para formar el mensaje encriptado.
    Los espacios entre palabras se representan con un punto y coma (;).
    
    Recibe:
        mensaje (str): El mensaje que se va a encriptar.
        
    Retorna:
        str: El mensaje encriptado.
    """