from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window

class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas:
            Rectangle(size=(Window.size[0], Window.size[1]),source="data/images/menu_bck.png", pos=(0,0))