from encriptar import encriptar_mensaje
from desencriptar import desencriptar_mensaje

def conversacion(mensaje, remitente, destinatario):
    print(f"{remitente} le manda a {destinatario}: {mensaje}")
    mensaje_encriptado = encriptar_mensaje(mensaje)
    print(f"{destinatario} recibe: {mensaje_encriptado}")
    mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado)
    print(f"{destinatario} desencripta y obtiene: {mensaje_desencriptado}")
    print()

if __name__ == "__main__":
    bob = "Bob"
    alice = "Alice"
    
    conversacion("hola", bob, alice)
    conversacion("Hola, cómo estas?", alice, bob)
    conversacion("Bien, gracias. Y tú?", bob, alice)
    conversacion("Mal, no pude ir al DCCarrete :(", alice, bob)