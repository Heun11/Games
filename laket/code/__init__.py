import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from .screens import GameScreen, MenuScreen

# Change Window size
Window.size = (1280, 750)
SCREEN_SIZE = Window.size

# Widnow Manaer
class WindowManager(ScreenManager):
    pass

# load kivy file
KV = Builder.load_file('main.kv')

# create basic app
class GameApp(App):
    def build(self):
        return KV
