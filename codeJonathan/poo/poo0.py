# --- DEFINITION ----



class Personne:
    bobo = "clown"

    def __init__(self, nom :str = "", age: int = 0):
        self.nom = nom #variable d'instance
    
        self.age = age
        print("Constructeur personne "+str(self.nom))
        if self.nom == "":
            self.nom = input("quel est votre prenom ?")

    #def demanderNom:

    def Sepresenter(self):
        presentation = "Bonjour je m'apelle "+self.nom
        if self.age == 0:
            print(presentation)
        else: 
            print(presentation+" j'ai "+str(self.age)+" ans")
            if self.estMajeur() : print("Je suis majeur")
            else: print("je suis mineur")

    def autrefonction(self):
        print(f"nom:{self.nom}")
    

    #def testdefonction(autrefonction):
    #    print("test"+str(autrefonction))
    #    print("test fonction")

    def quelageatu(self):
        print("tu as "+str(self.age)+"age")
        
    
    def estMajeur(self):
        return self.age >= 18

#--- UTILISATION ---

personne1 = Personne("Jean", 35) #je crée une personne
personne2 = Personne("Paul", 15) #je crée une personne

Personne.Sepresenter(personne1)         #même chose que plus bas
#personne1.Sepresenter()                 #même chose que plus haut

Personne.Sepresenter(personne2)
"""personne2.Sepresenter()


Personne.autrefonction(personne1)
personne1.autrefonction()
Personne.autrefonction(personne2)
personne2.autrefonction()

#Personne.testdefonction(personne1)
#personne1.testdefonction()

personne2.quelageatu()

print(personne1.estMajeur())
print(personne2.estMajeur())"""

personne4 = Personne()
personne4.Sepresenter()
personne4 = Personne(age = 20)
personne4.Sepresenter()
print(personne1.bobo)
personne1.bobo = "toto"
print(personne1.bobo)
print(personne2.bobo)
Personne.bobo = "coco"
personne5 = Personne()
print(personne5.bobo)