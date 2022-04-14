stoplist = ['le', 'la', 'les', 'un', 'une', 'des', 'de', 'se',
            'sa', 'son', 'et', 'ou', 'à', 'ne', '!', '?', '.',
            ';', "'"]
# j'ai ajouté a la variable stoplist, tout les articles qui me semble pertinante,
# ainsi que les articles de possessions, et que quelque prépositions,
# afin de garder que les mots intéréssant, il y en a d'autre,.
# mais j'ai gardé ceux qui sont intéréssant pour le texte cigale_fourmi.txt

def pilote(fichier, idx):
    with open(fichier, 'r', encoding='utf8') as fp:
        # on itere sur le fichier ligne par ligne
        for i, ligne in enumerate(fp):
            indexe(idx, ligne.split(), i)

def ajoute(idx, mot, ligne):
    # si le mot ne se trouve pas encore dans l'index, 
    # initialise les occurences par une liste vide
    if mot not in idx:
        idx[mot] = []
    # si la ligne n'a pas encore ete enregistree pour ce mot
    if ligne not in idx[mot]:
        # on ajoute le numero de ligne correspondant au mot
        idx[mot].append(ligne)

def indexe(idx, mots, ligne):
    # on itere sur les mots
    for mot in mots:
        # met obligatoirement en minuscule
        mot = mot.lower()
        # nettoyage du mot, voir ci-apres
        mot = nettoie(mot)
        # on en profite pour verifier si on veut 
        # vraiment indexer ce mot
        if mot and mot not in stoplist:
            ajoute(idx, mot, ligne)

def nettoie(mot):                      
    test0 = """(")!/+,."""
    test = ["l'", "d'"]
    finmot = ''
    for x in mot:                      
            if x not in test0:
                finmot = finmot + x
            else:
                pass
    
    mot = finmot
    for x in test:
        if x in mot[:2]:
            mot = mot[2:]
    return mot


def prd(idx):
    for mot in sorted(idx):
        print('\t', mot, ':', idx[mot])

index = {}
pilote('C:/Users/User/Documents/cigale_fourmi.txt', index)
prd(index)