import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from .game import GameScreen
from .menu import MenuScreen

# COMENT THIS WHEN GOING ON PHONE
Window.size = (1920*0.7, 1080*0.7)

class WindowManager(ScreenManager):
    pass

KV = Builder.load_file('main.kv')

class GameApp(App):
    def build(self):
        return KV
