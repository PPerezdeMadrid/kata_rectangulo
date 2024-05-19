import socket
import sys
import os

def main():
    direcc_serv = '127.0.0.1'
    puerto = input("Introduzca el puerto de su servidor: ")
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((direcc_serv, int(puerto)))
    
    print(f'Su dirección local es: {cli_socket.getsockname()}') 

    nick = input("Introduzca su nombre de usuario (nick): ")
    mensaje = input("==> ")
    estructura_mensaje = nick + ": " + mensaje

    cli_socket.sendall(estructura_mensaje.encode()) # Cambiamos a sendall!
   
    while True:
        mensaje_del_servidor = cli_socket.recv(1024)
    
if __name__ == "__main__":
    main()

# Ejemplo: /etc/libreoffice/registry/main.xcd

"""
Vamos a crear una estructura de Mensaje:
Enviaremos: {nick}: {mensaje}
"""
