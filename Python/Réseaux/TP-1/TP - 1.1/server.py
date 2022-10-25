# Echo server program
import socket
from random import *

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 50001  # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        INTERVAL_MIN = randint(1, 3)
        INTERVAL_MAX = randint(6, 10)
        NB_MYSTERE = randint(INTERVAL_MIN, INTERVAL_MAX)
        trouve = 0
        restant = 5

        while trouve != 1 and restant != 0:

            data = conn.recv(1024)[2:-1]

            if int(data) == NB_MYSTERE:
                trouve = 1
                msg = f'{INTERVAL_MIN}={INTERVAL_MAX}={restant}={trouve}'

            if not data or data == 1 or restant == 0: break

            else:
                restant -= 1
                msg = f'{INTERVAL_MIN}={INTERVAL_MAX}={restant}={trouve}'

            conn.sendall(bytes(msg, 'utf-8'))
