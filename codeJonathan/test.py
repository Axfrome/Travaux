def extraireExtension(element):
    if "." in element:
        b =str(element).split(".")
        return str(b[-1]).lower()
    else:
        return "Aucune extension"


def recupereIndex(liste, element):

    listetemp = []
    #met la liste en minuscule
    for x in liste:
        x = str(x).lower()
        listetemp.append(x)
    return listetemp.index(str(element).lower())

def quoiExtension(listeextension, extension):
    if extension == "Aucune extension":
        return "Aucune extension"
    for x in listeextension:
        if str(extension).lower() in x:
            return x[1]
    return "Extension non connu"

def donneeAffichage(listefichiers, listeextension):
    listDonneAffichage = []
    for element in listefichiers:
        extension = extraireExtension(element)
        indexaton = recupereIndex(listefichiers, element)
        quoiCorrespondExtension = quoiExtension(listeextension, extension)
        listDonneAffichage.append([element,quoiCorrespondExtension])
    return listDonneAffichage

def AffichageEntier(donnee):
    print()
    for nomEtType in donnee:
        print(str(nomEtType[0])+" ("+str(nomEtType[1])+") ")

fichiers = ("notepad.Exe", "mon.fichier.perso.doc", "notes.TXT", "vacance.jpeg", "planning", "data.dat")   

definitionExtension = (("doc", "Document Word"), ("exe","Executable"), ("txt", "document texte"), ("jpeg", "image JPEG"))

donneAafficher = (donneeAffichage(fichiers, definitionExtension))
AffichageEntier(donneAafficher)


"""
notepad.Exe (executable)
mon.fichier.perso.doc (Document Word)
note.txt (document texte)
vacances.jpeg (image JPEG)
planning (aucune extension)
data.dat (extension non connu)
"""
