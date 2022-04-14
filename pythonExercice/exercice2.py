# -*- coding:Latin-1 -*-
# -*- coding:Latin-1 -*-
secondeDepart = 50000000

secondeJour = 86400

nbJour = secondeDepart/secondeJour

print(nbJour, "nombre de jour total")

nombreAnnee = (nbJour/365)
resteNombreDeJours = nbJour%365

print(nombreAnnee, "c'est le nombre d'année")

print("il reste", resteNombreDeJours, "jours")
Mois = resteNombreDeJours/30

print ("il reste", Mois, "mois")

resteMois = resteNombreDeJours%30

resteMoisjour = resteMois-int(resteMois)

print("il reste", int(resteMoisjour*30), "jours")

resteH = ((resteMoisjour*30)-(int(resteMoisjour*30)))*24

print("il reste", resteH,"heures")

restemin = resteH - int(resteH)

print("reste min", restemin*30)