import os
import subprocess

#Popen : ancienne interface.
# run : executer la commande et attendre le resultat
while True:
    command_terminal = input(os.getcwd() + " > ")
    if command_terminal == "exit": 
        break

    commande_split = command_terminal.split(" ")
    if len(commande_split)  == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except(FileNotFoundError):
            print("Fichier introuvable")

    else:
        resultat = subprocess.run(command_terminal, shell=True, capture_output=True)
        print(resultat.stdout.decode("utf-8", errors='ignore'))