import socket
import sys
import ast

def enviar_mensaje_a_todos(mensaje):
    for cliente in conexiones_clientes:
        print("Type" + str(type(cliente)))
        envio = cliente.send(mensaje.encode())
        print("broadcast sendall " + str(envio))
        # deberiamos poner unos try

def conexion_cliente(conexion):
    data, _ = conexion.recvfrom(1024) # Hay limite???
    # data debería ser:"nick: mensajeconexiones
    print("Servidor ha recibido << "+ data.decode()+ " >>\n")

    enviar_mensaje_a_todos(data.decode())
    

    
def main():

    direcc_socket = '127.0.0.1' 
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direcc_socket, 0))
    print(f'la dirección local es {servidor.getsockname()}')

    max_conexiones = int(input("Ingrese el número máximo de conexiones pendientes: "))
    servidor.listen(max_conexiones)
    

    try:
        while True:
            conexion, direcc_cli = servidor.accept()
            conexiones_clientes.append(conexion)
            conexion_cliente(conexion)

    except KeyboardInterrupt:
        print("Cerrando el servidor...")
        servidor.close()

if __name__ == "__main__":
    conexiones_clientes = []
    main()


