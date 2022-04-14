from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.behaviors import CoverBehavior
from http_client import HttpClient
from storage_manager import StorageManager

from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str= StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """self.pizzas = [
            Pizza("4 fromages", "brie, chèvre, emmental, comté", 9.5, True),
            Pizza("chorizo", "tomates, chorizo parmesan", 11.2, False),
            Pizza("Calzone", "fromage, champignon,  crème", 10, False)
        ]"""
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)
    
    def on_parent(self, widget, parent):
        #low = [pizza.get_dictionnary() for pizza in self.pizzas]
        pizzas_dict =StorageManager().load_data("pizzas")
        if pizzas_dict:
            self.recycleView.data = pizzas_dict
        

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)
        
    def on_server_error(self, error):
        self.error_str = "ERREUR: " + error
        

class PizzaApp(App):
    pass


PizzaApp().run()