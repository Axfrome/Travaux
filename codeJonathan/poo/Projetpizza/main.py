#nom, prix, ingredients, végétarienne



class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Affichier(self):
        veg_str = ""
        if self.vegetarienne == True:
            veg_str = "- Vegetarienne"
        print(f"PIZZA {self.nom} : {self.prix} €" + veg_str)
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__("Personnalisé " + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()
    
    def demander_ingredients_utilisateur(self):
        print()
        print("ingredient pour la pizza personnalisé numéro : " + str(self.numero))
        while True:
            ingredient = input("Ajouter 1 ingrédients (ou ENTER POUR TERMINER) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            (f"vous avez {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
        self.prix = ((self.PRIX_DE_BASE + (len(self.ingredients)*self.PRIX_PAR_INGREDIENT)))

pizza1 = Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True)

#pizza1.Affichier()
pizzas = [(Pizza("miel", 9.0, ("miel", "tomate", "olive",), True)), 
          (Pizza("bolognaise", 11.5, ("viande haché", "tomage", "fromage"))), 
          (Pizza("Mozarella", 12, ('tomate', 'mozarela', 'olive', 'gruyere'), True)),
          (PizzaPersonnalisee()),
          (PizzaPersonnalisee())]
#def tri(e):
#    return len(e.ingredients)
#pizzas.sort(key = tri)

for x in pizzas:
    x.Affichier()