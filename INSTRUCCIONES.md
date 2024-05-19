### Manual de Usuario

#### Ejecución del Cliente
Para ejecutar el cliente, introduce el siguiente comando en la línea de comandos:
```sh
make cliente SOCKET_DIR=<<direccion_socket>>
```
Por ejemplo:
```sh
make cliente SOCKET_DIR=/tmp/socket_pr4
```
Escribe algo y recibirás la hora (si el servidor está ejecutándose).

#### Ejecución del Servidor
Para ejecutar el servidor, introduce el siguiente comando en la línea de comandos:
```sh
make servidor SOCKET_DIR=<<direccion_socket>>
```
Por ejemplo:
```sh
make servidor SOCKET_DIR=/tmp/socket_pr4
```

Asegúrate de ejecutar el servidor antes de iniciar el cliente para que funcione correctamente.