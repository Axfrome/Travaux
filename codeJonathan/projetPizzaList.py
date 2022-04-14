def ajouterPizzaUtilisateur(pizza : list, ajouter : str) -> list :
    pizzaaajouter = input("quel est la pizza que vous voulez ajouter ? " )
    pizza.append(ajouter)

def afficher(collection):
    if len(collection) == 0:
        print("Aucune pizza")
        return
    print("LISTE DE PIZZAS", len(collection))
    for x in collection:
        print(x)





pizzas = ["4 fromages","Végétarienne","Hawai","Calzone"]
pizzas2 = []
ajouterPizzaUtilisateur(pizzas, "bolognaise")
afficher(pizzas)