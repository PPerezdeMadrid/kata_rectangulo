import os

"""
Pipe1: Cliente ---> Servidor
Pipe2: Servidor --> Cliente
"""

def cliente_servidor():
    r_pipe1, w_pipe1 = os.pipe() # cliente-servidor
    r_pipe2, w_pipe2 = os.pipe() # servidor-cliente
    
    r1, w1 = os.fdopen(r_pipe1, 'r'), os.fdopen(w_pipe1, 'w') # cliente-servidor
    r2, w2 = os.fdopen(r_pipe2, 'r'), os.fdopen(w_pipe2, 'w') # servidor-cliente

    if os.fork():
        # Soy el hijo 
        # Envío solicitud del pipe
        os.close(r1)
        os.close(w2)

        w1.write('/bin/sh')
        os.close(w1)
        
        


    



