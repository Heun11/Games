from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock
import time

from .classes import Game

# Menu
class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas:
            Rectangle(size=(Window.size[0], Window.size[1]),source="data/images/menu_bck.png", pos=(0,0))

# Game
class GameScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FPS = 60
        self.screen_size = Window.size
        self.game=Game(sc=self.screen_size)
        self.dead_text=Label(text="",pos_hint={"y":0.7, "x":0.4},size_hint=(0.2,0.1))
        self.score=Label(text="",pos_hint={"y":0.9, "x":0.9},size_hint=(0.1,0.1))

    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_interval(self.update,1/self.FPS)

    def update(self, dt):
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
            self.game.update(dt)

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        self.game.on_touch_down(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        self.game.on_touch_up(touch)
