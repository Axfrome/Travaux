#Nom : ATALAY , Prénom : Tuncay Numéro : 20008360

import requests
import re



def pilote(page):
    
    # ouvre une requête sur l'URL spécifiée
    r = requests.get(page)

    # si la requête a abouti sans erreur
    if r.ok:
        # récupère le texte de la page
        a = r.text
    else:
        # affiche l'erreur (facultatif)
        print('erreur', r.reason)

 
    return a

#jusque là ça vas, plus bas il vas y avoir beaucoups de traitement de chaine de caractere

def extraire_liens(a):
    #initialisation de variable
    listeliens= []
    liens = ""
    test2 = ""
    x = 0
    C = 0
    C2 = 0
    test = """href="https"""
    #reconnaissance HREF
    while x < len(a)-10:
        test2 = ""
        C = x
        while C < x+11:
            test2 = test2+a[C]
            C = C+1        
        if test == test2:
    #HREF si reconnue, on enregistre le lien.
                C2 = x
                #en cas de chevrons non fermante on ne fais rien
                while C2 < len(a):
                    if C2 == len(a):
                        liens = ""
                        break
                    liens = liens+a[C2]
                    C2 = C2+1
                    #une fois le liens récupéré on l'ajoute à la liste.
                    if a[C2-1] == ">":
                        listeliens.append(liens)
                        liens = ""
                        break
        #lettre suivante
        x = x+1
    return listeliens


def nettoie_page(listeliens):
    bernadette = 0
    newjersey = []
    #suppression de la balise HREF pour chaque élement dans la liste
    #et suppression de chevrons fermante
    for britney in listeliens:        
        newjersey.append((listeliens[bernadette][6:-2]))
        bernadette = bernadette + 1
    dernierliens = []
    #un deuxieme couche de nettoage est necessaire
    #nottamment après .com ect ...
    #mise en forme suivante
    for carole in newjersey:
        y = 0
        finalien = ""
        for p in carole:
            if p == '"':
                dernierliens.append(finalien)
                break
            finalien = finalien + p
            y = y+1
    y = 0
    
    #afficher les liens recu
    for x in dernierliens:
        print (y, dernierliens[y])
        y = y+1

#cette fonction sert uniquement a recuperer le premier liens contenu dans l'indexage
# et de le nettoyer afin d'en garder que le site web pour que l'indexage puisse
# avoir lieu pour le premier lien rencontre.
def retiensliens(listeliens):
    bernadette = 0
    newjersey = []
    for britney in listeliens:
        newjersey.append((listeliens[bernadette][6:-2]))
        bernadette = bernadette + 1
    dernierliens = []
    #mise en forme suivante
    for carole in newjersey:
        y = 0
        finalien = ""
        for p in carole:
            if p == '"':
                dernierliens.append(finalien)
                break
            finalien = finalien + p
            y = y+1
    y = 0

    return dernierliens[0]

#l'indexage vas indexer le site web, et ajouter l'indexage
# les deux sous-liens et sous-sous liens present dans le site racine.
def index(siteweb):
    # on récupere la liste de liens du site web
    a = (extraire_liens(pilote(siteweb)))
    b = retiensliens(extraire_liens(pilote(siteweb)))
    c = extraire_liens(pilote(b))
    d = retiensliens(c)
    e = extraire_liens(pilote(d))
    f = a + c + e
    nettoie_page(f)

#l'affichage du programme
print("bienvenue dans mon programme")
wait = input("PRESS ENTER TO CONTINUE.")
print ("ce programme indexe les liens contenus dans le site web et index également le premier lien reconnu dans le site")
print ("voici l'exemple avec plusieurs site dont le site wiki de paris8 : https://fr.wikipedia.org/wiki/Universit%C3%A9_Paris-VIII ")
wait = input("PRESS ENTER TO CONTINUE.")
index('https://fr.wikipedia.org/wiki/Universit%C3%A9_Paris-VIII')
print ("puis celle de https://www.facebook.com/")
wait = input("PRESS ENTER TO CONTINUE.")
index('https://www.facebook.com/')
print ("ou encore le site de wikipedia (page d'acceuil), attention il y a plus de 1000 liens")
wait = input("PRESS ENTER TO CONTINUE.")
index('https://fr.wikipedia.org/')
print("voilà le programme est fini appuyer sur une touche pour finir")
wait = input("PRESS ENTER TO CONTINUE.")