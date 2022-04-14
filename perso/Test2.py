mot = "boucherie"

def retournermot(mot):
    return print(mot[::-1])

retournermot(mot)

nbMot = len(mot)-1
nvmot = ""

while nbMot >= 0:
    nvmot = nvmot + mot[nbMot]

print(nvmot)