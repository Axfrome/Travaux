# -*- code:latin1 -*-
###
# VOS PREMIER PAS EN POO (PROGRAMMATION ORIENTEE OBJET)
###
# - Différence programmation imperative / objet.
# - Le plus simple possible.
# - Exercices, mises en situation.

# Personne (entité --> class)
#       Données : Nom, Age
#       Actions (méthodes) : sePrésenter, demanderNom/input

#          ETRE VIVANT              #CLASSE PARENT
#     Chat          Personne        #CLASSE ENFANT (classe dérivées)
#

# --- DEFINITION ---
from tkinter.constants import FALSE, TRUE

class EtreVivant:
    ESPECE = "(être vivant non identifié)"

    def afficherInfosEtrevivant(self):
        print("info être vivant :"+self.ESPECE)

class Chat(EtreVivant):
    ESPECE = "chat (mammifères)"   #variable de classe (1 pour toute les classe)

class Personne(EtreVivant):
    ESPECE = "humain (mammifères)"   #variable de classe (1 pour toute les classe)
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom #crée une variable d'instance nom.
        self.age = age
        if nom == "":
            self.demanderNom()

        print(f"Constructeur {self.nom}, {self.age}")
    def sePresenter(self):
        infopersonne = "bonjour je m'apelle "+self.nom
        if self.age == 0:
            print(infopersonne)
        else:
            print(infopersonne+" j'ai", str(self.age), "ans")
            if self.estMajeur() == FALSE:
                print("je suis mineur")
            else:
                print("je suis majeur")
    def estMajeur(self):
        if self.age <= 18:
            return FALSE
        else:
            return TRUE
    def demanderNom(self):
        self.nom = input("Nom inexistant, Ecrivez un nom : ")

#etrevivant
#personne
#etudiant
class Etudiant(Personne):
    def __init__(self, nom : str = "" , age : int = 0, etudes: str = ""):
        super().__init__(nom, age)
        self.etudes = etudes
    
    def sePresenter(self):
        super().sePresenter()
        print("Je suis étudiant en "+self.etudes)

# --- UTILISATION ---

personne1 = Personne("Jean", 30)
personne2 = Personne("Paul", 15)
personne3 = Personne("Estelle", 25)
#personne1.sePresenter()
#personne2.sePresenter() #Méthode d'instance

#Personne.espece = "coucou" modification de variable de classe.
listePersonnes = (personne1, personne2, personne3)
print()
for personne in listePersonnes:
    personne.sePresenter()
    personne.afficherInfosEtrevivant()
    print()

chat1 = Chat()
chat1.afficherInfosEtrevivant()

etrevivant = EtreVivant()
etrevivant.afficherInfosEtrevivant()

etudiant = Etudiant("marc", 22, "Ecole d'ingénieur informatique")
etudiant.sePresenter()

#Personne.autrefonction() #Methode de classe ou statique

"""def afficherInformationPersonne(nom, age):
    print(f"La personne s'apelle {nom}, son age est {age} ans")


def demanderNomPersonne():
    nom = input("quel est votre nom? ")
    return nom

nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

nom3 = demanderNomPersonne()
age3 = 20

afficherInformationPersonne(nom1, age1)
afficherInformationPersonne(nom2, age2)
afficherInformationPersonne(nom3, 38)"""