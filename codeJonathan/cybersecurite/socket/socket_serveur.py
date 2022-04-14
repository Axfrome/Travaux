#Exercice pas parfais.
# -*- coding: utf-8 -*-
from multiprocessing import connection
import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def serveur_():
    s = socket.socket()
    s.bind(("127.0.0.1", 32000))
    s.listen()
    print(f"Attente de connection sur {HOST_IP} par le port {HOST_PORT} ... ")
    connection_socket, client_adress = s.accept()
    print(f"Connection etablie avec {client_adress}")



    texte_envoye = input("Vous : ")
    connection_socket.sendall(texte_envoye.encode())    
    s.close()
    connection_socket.close()

def client_():
    s = socket.socket()
    while True:
        try:
            print(f"Connection au serveur {HOST_IP}, au PORT :  {HOST_PORT}")
            s.connect((HOST_IP, HOST_PORT))
        except ConnectionRefusedError:
            print("Erreur impossible de se connecter au serveur")
            time.sleep(4)
        else:
            break
    date_recues = s.recv(MAX_DATA_SIZE)
    print(date_recues.decode())
    s.close()

while True:
    serveur_()
    client_()