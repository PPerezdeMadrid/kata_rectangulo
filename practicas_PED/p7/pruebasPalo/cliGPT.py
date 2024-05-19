import socket

def recibir_mensajes(socket_cliente, nick):
    while True:
        try:
            mensaje = socket_cliente.recv(1024).decode()
            print(f'==> {nick}: {mensaje}')
        except:
            print('¡Error al recibir mensajes del servidor!')
            socket_cliente.close()
            break

def main():
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    puerto_servidor = int(input("Indique el puerto del servidor: "))
    socket_cliente.connect(('localhost', puerto_servidor))

    nick = input('Ingrese su nombre de usuario (nick): ')
    socket_cliente.send(nick.encode())

    print(socket_cliente.recv(1024).decode())

    recibir_mensajes(socket_cliente, nick)

    while True:
        mensaje = input(nick + ": ")
        socket_cliente.send(mensaje.encode())

if __name__ == "__main__":
    main()

