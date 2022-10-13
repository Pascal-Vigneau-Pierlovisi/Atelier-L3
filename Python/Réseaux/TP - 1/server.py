# Echo server program
import socket
from Cmd import Cmd

CMD = Cmd()  # On déclare un objet de type CMD
HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 50008  # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(type(data))
            if not data: break
            mess = Cmd.executeCmd(CMD, data)
            conn.sendall(bytes(mess, 'utf-8'))
