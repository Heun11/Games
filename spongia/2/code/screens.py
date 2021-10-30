from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import ObjectProperty

from .musics import Music, MusicLoader

# Menu
class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas:
            Rectangle(size=(Window.size[0], Window.size[1]),source="data/images/menu_background.png", pos=(0,0))

# Game
class GameScreen(Screen):
    code=ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.FPS = 30
        self.screen_size = Window.size
        self.sample_audio = Music(MusicLoader.load(0))

    def play_sample_audio(self):
        self.sample_audio.play()

    def stop_sample_audio(self):
        self.sample_audio.stop()

    def update(self, dt):
        fps = int(1/dt)
        print(fps)