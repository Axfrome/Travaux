liste = [1, 2, 3, 4]

minimum = 0
median = 0
maximum = 0
x = 0
listetemp = []
while x < len(liste)-1: 
#je met le comparateur < car le curseur vas chercher toujours la chiffre suivant
#le probleme c'est lorsqu'il est en fin de liste il me fais un out of limit.
#donc le dernier élément de la liste je dois le prendre séparément.
    if x == 0: #au début j'initialise ma valeur minimal de la liste
        minimum = liste[x]
    if x > 0: #puis les élements suivant de la liste
        if liste[x] == liste[x+1]-1:
            #c'est une suite
            median = liste[x]
            #la valeur median est la valeur temporaire maximal
            #elle seras remplacé tant que la suite reste une suite
    x = x+1

# pour l'instant la valeur median reste a 3

if x == len(liste)-1: #c'est le dernier element de la liste
    #normalement x = 3 alors on seras au dernier element de la liste de tte façon.
    if liste[x] == liste[x-1]+1:
        median = liste[x] # on confirme que le dernier élément est une suite)
    # on sais que la liste est fini alors pour cette exemple median deviens max
        maximum = median

#on a deux valeur maximum et minimum qui sont de 1 et 4 faut en faire une liste.

listetemp.extend([[minimum, maximum]])

print (listetemp)

if len(listetemp[0]) == 2: #si ya deux elements dans la liste
    #ma methode étais de crée 2 partie en string
    premier = str([listetemp[0][0]])
    deuxieme = str([listetemp[0][1]])
    #une fois les deux partie crée tu dois faire un traitement de caractere comme ceci:
    #avec concaténation bien sur.
    print (premier[1:-1]+'-'+deuxieme[1:-1])