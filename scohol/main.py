import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from random import randint
from kivy.core.audio import SoundLoader
import json

Window.size = (1280, 720)

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        FPS = 30
        self.screen_width = Window.size[0]
        self.screen_height = Window.size[1]
        Clock.schedule_interval(self.update,1/FPS)

        self.show_inv = False

    def update(self,dt):
        # DRAW
        self.canvas.clear()
        with self.canvas:
            Rectangle(pos=(0,self.screen_height-50), size=(100,50))

        # UPDATE

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        if touch.pos >= (0,0):
            print("ok")

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)


class MenuWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
