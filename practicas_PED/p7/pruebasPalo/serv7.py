import socket

def enviar_mensaje_a_todos(mensaje):
    for cliente in clientes:
        cliente.send(mensaje.encode())
        # deberiamos poner unos try

def conexion_cliente(socket_cli, direcc_cli):
    nick = socket_cli.recv(1024).decode() # Cliente envía su nick
    print(f'{nick} se ha conectado desde {direcc_cli}')
    
    enviar_mensaje_a_todos(f'{nick} se ha unido al chat.')

    while True:
        try:
            mensaje = b''
            while True:
                particion = socket_cli.recv(1024).decode()
                if not particion:
                    break
                mensaje =+ particion

            if mensaje:
                enviar_mensaje_a_todos(f'{nick}: {mensaje.decode()}')
        except:
            socket_cli.close()
            break

def main():
    direcc_serv = '127.0.0.1'
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direcc_serv, 0))
    print(f'la dirección local es {servidor.getsockname()}')

    max_conexiones = int(input("Ingrese el número máximo de conexiones pendientes: "))
    servidor.listen(max_conexiones)

    try:
        while True:
        socket_cli, direcc_cli = servidor.accept()
        clientes[socket_cli] = direcc_cli
        conexion_cliente(socket_cli, direcc_cli)
        
    except KeyboardInterrupt:
        print("Cerrando el servidor...")
        # cerrar todos los clientes
        
if __name__ == "__main__":
    clientes = {}
    main()
