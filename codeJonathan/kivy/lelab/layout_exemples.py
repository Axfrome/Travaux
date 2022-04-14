from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

Builder.load_file("layout_exemples.kv")

class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation="rl-tb"
        for i in range(0, 100):
            b= Button(text=str(i+1), size_hint=(None, None), size=(dp(60), dp(60)))
            self.add_widget(b)

class GridLayoutExemple(GridLayout):
    pass

class AnchorLayoutExemple(AnchorLayout):
    pass

class BoxLayoutExemple(BoxLayout):
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation= "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""
    pass

