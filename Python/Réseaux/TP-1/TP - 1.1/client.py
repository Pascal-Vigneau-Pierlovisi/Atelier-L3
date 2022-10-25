# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50001              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    trouve = 0
    restant = 5
    print("---Lancement de la partie---")
    while trouve != 1 and restant != 0:
        user = input("Votre nombre : ")
        s.sendall(bytes(user, 'utf-8'))
        data = s.recv(1024)[2:-1]
        print(data)
        if(int(data[3]) == 1):
            print("Bravo le nombre est trouvé !")
            trouve = 1
        else:
            print("Le nombre n'est pas bon ...")
            print(f'Il est compris entre {data[0]} et {data[1]}')
        restant = data[2]

