# Echo client program
import socket

HOST = 'localhost'  # The remote host
PORT = 50008  # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'LOWER HELLO WORLD') Test avec la commande LOWER
    # s.sendall(b'UPPER hello world') Test avec la commande UPPER
    # s.sendall(b'DATENOW') Test avec la commande DATENOW
    s.sendall(b'Hello World')

    data = s.recv(1024)
print('Received', repr(data))
