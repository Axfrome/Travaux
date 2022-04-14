import requests
import re

def extraire_liens(page):
    
    # ouvre une requête sur l'URL spécifiée
    r = requests.get(page)

    # si la requête a abouti sans erreur
    if r.ok:
        # récupère le texte de la page
        a = r.text
    else:
        # affiche l'erreur (facultatif)
        print('erreur', r.reason)

    texte = re.sub("<.*?>","",a)
 
    
    listeliens= []
    liens = ""
    test2 = ""
    x = 0
    C = 0
    C2 = 0
    test = """<a href="https"""
    #reconnaissance HREF
    while x < len(a)-13:
        test2 = ""
        C = x
        while C < x+14:
            test2 = test2+a[C]
            C = C+1        
        if test == test2:
    #HREF si reconnue, on enregistre le lien.
                C2 = x
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
        x = x+1
    return listeliens


def nettoie_page(listeliens):
    bernadette = 0
    newjersey = []
    for britney in listeliens:
        newjersey.append((listeliens[bernadette][9:-2]))
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
    for x in dernierliens:
        print (dernierliens[y])
        y = y+1
                

a = (extraire_liens('https://fr.wikipedia.org/wiki/Universit%C3%A9_Paris-VIII'))
nettoie_page(a)