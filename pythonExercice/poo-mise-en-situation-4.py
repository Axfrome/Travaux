# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []
nombrePersonne = 4

for i in range(nombrePersonne):
    noms.append(input(f"nom de la personne {i+1} : "))
l = []

for nom in noms:
    l.append(Personne(nom))

for p in l:
    p.SePresenter()
