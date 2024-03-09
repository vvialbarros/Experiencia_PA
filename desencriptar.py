

def desencriptar_mensaje(mensaje_encriptado: str) -> str:
    """
    Esta función toma un mensaje encriptado como entrada y lo desencripta utilizando un libro_super_secreto.txt. 
    Cada letra del mensaje original viene codificada como string con la siguiente estructura:
    
    "numero_linea,numero_palabra,numero_letra_en_palabra"
    
    Donde:
    - numero_linea es la línea en la que se encuentra la letra en el libro.
    - numero_palabra es la palabra en la que se encuentra la letra en la línea.
    - numero_letra_en_palabra es la posición de la letra en la palabra.
    
    Luego se debe buscar en el libro la letra correspondiente a cada string y concatenar todas las letras para formar el mensaje original.
    Los espacios del mensaje original se representan con un punto y coma (;).
    
    Recibe:
        mensaje_encriptado (str): El mensaje que se va a desencriptar.
        
    Retorna:
        str: El mensaje desencriptado.
    """
