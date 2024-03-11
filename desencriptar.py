

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
    Los numeros parten desde 0.
    
    Por ejemplo, la frase codificada 12,0,0,0,1,11,0,11,6;0,1,2,0,1,3,0,1,5,0,1,11,0,11,6;0,2,0,0,1,11,0,1,7,0,3,1,0,1,9,0,1,3,0,1,4,3,6,6,0,1,9;0,1,1,0,0,1;0,1,7,0,6,4,0,1,9,0,2,0,0,1,11
    se desencripta como:
    Linea 12, palabra 0, letra 0 -> L
    Linea 0, palabra 1, letra 11 -> o
    Linea 0, palabra 11, letra 6 -> s
    ; -> espacio
    Siguiendo se obtiene el mensaje original "Los patos dominarán el mundo" 
    
    Recibe:
        mensaje_encriptado (str): El mensaje que se va a desencriptar.
        
    Retorna:
        str: El mensaje desencriptado.
    """
