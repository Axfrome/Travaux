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

Builder.load_file("widget_exemples.kv")

class WidgetExemple(GridLayout):
    mon_texte= StringProperty("1")
    chiffre = 2
    toggle = BooleanProperty(False)
    text_input_str = StringProperty("toto")
    #slider_value_txt = StringProperty("Valeur")
    
    def on_button_click(self):
        if self.toggle == True:
            print("Button click")
            self.mon_texte= str(self.chiffre)
            self.chiffre = self.chiffre+1
    
    def on_toggle_button_state(self, widget):
        #print('toggle state: '+ widget.state)
        if widget.state == "normal":
            print("OFF")
            widget.text="OFF"
            self.toggle = False
        else:
            print("ON")
            widget.text="ON"
            self.toggle = True
    def on_switch_active(self, widget):
        print("switch: "+ str(widget.active))
    
    def on_slider_value(self, widget):
        print('slider: '+str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))
    def on_text_validate(self,widget):
        self.text_input_str = widget.text