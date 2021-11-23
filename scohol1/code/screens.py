from posixpath import supports_unicode_filenames
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock
import random

from .entity import Entity

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
        self.FPS = 30
        self.sc = Window.size

        self.player = Entity(sc=self.sc, pos=[0.1, 0.27])
        self.player_move=""

        self.background_image = "bck1"

    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_interval(self.update,1/self.FPS)

    def update(self, dt):
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
            Rectangle(size=self.sc, source=f"data/images/{self.background_image}.png")

            self.player.update()

            if self.player_move=="r":
                self.player.pos[0]+=self.sc[0]*0.005
            
            elif self.player_move=="l":
                self.player.pos[0]-=self.sc[0]*0.005

        print(1/dt)


    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        if touch.pos[0]>self.sc[0]*0.5:
            self.player_move="r"

        else:
            self.player_move="l"

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        self.player_move=""
