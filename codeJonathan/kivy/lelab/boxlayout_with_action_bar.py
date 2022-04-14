from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from navigation_screen_manager import NavigationScreenManager

Builder.load_file("boxlayout_with_action_bar.kv")

class BoxLayoutWithActionBar(BoxLayout):
    title = StringProperty()