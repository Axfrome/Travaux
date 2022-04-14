import requests
import re

def nettoie_page(page):
# ouvre une requête sur l'URL spécifiée
    r = requests.get(page)

    # si la requête a abouti sans erreur
    if r.ok:
        # récupère le texte de la page
        text = r.text
    else:
        # affiche l'erreur (facultatif)
        print('erreur', r.reason)

    texte = re.sub("<.*?>","",text)

    print(texte)

nettoie_page('https://fr.wikipedia.org/wiki/Universit%C3%A9_Paris-VIII')