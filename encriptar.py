
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
    Los numeros parten desde 0.
    
    Por ejemplo, la frase "Los patos dominarán el mundo" se encripta como:
    12,0,0,0,1,11,0,11,6;0,1,2,0,1,3,0,1,5,0,1,11,0,11,6;0,2,0,0,1,11,0,1,7,0,3,1,0,1,9,0,1,3,0,1,4,3,6,6,0,1,9;0,1,1,0,0,1;0,1,7,0,6,4,0,1,9,0,2,0,0,1,11
    Linea 12, palabra 0, letra 0 -> L
    Linea 0, palabra 1, letra 11 -> o
    Linea 0, palabra 11, letra 6 -> s
    ; -> espacio
    
    Recibe:
        mensaje (str): El mensaje que se va a encriptar.
        
    Retorna:
        str: El mensaje encriptado.
    """