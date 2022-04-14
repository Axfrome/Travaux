def afficher(nom, age):
    print()
    print(f"{nom} vous avez {age} ans")
    print(nom+" vous aurez l'an prochain "+str(age+1)+"ans")
    if age < 10 :
        print("vous etes un enfant")
    elif age > 60 :
        print("vous etes un senior")
    elif age == 17:
        print("vous etes presque majeur")
    elif age == 18:
        print ("tout juste majeur, félicitation")
    elif age > 18:
        print("vous etes majeurs")
    else:
        print("vous etes mineur")

def demanderage(nom):
    ageprochain = 0
    while ageprochain == 0:
        agestr = input(nom + " quel est votre age ?")
        try:
            age = int(agestr)
            ageprochain = 1
        except:
            print("ERREUR :entrez un nombre ")
    return age

def demandernom():
    #Demander nom
    nom = ""
    while nom == "":
        nom = input("entrez votre nom ")
        #age = input("entrez votre age ")
    return nom

nom1 = demandernom()
nom2 = demandernom()
#Demander age
age = demanderage(nom1)
age2 = demanderage(nom2)

afficher(nom1, age)
afficher(nom2, age2)