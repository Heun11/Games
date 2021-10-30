from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock
import json

from .sceneloader import SceneLoader

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
        with open("data/save.json") as f:
            self.ac_scene = json.load(f)["ac_scene"]
        self.scene_loader = SceneLoader(self.screen_size)

    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_interval(self.update,1/self.FPS)

    def update(self, dt):
        self.canvas.clear()
        self.clear_widgets()
        self.add_widget(Label(text=f"{int(1/dt)}", pos_hint={"y":0.9}, size_hint=(0.1,0.1)))
        with self.canvas:
            self.scene_loader.update(self.ac_scene)

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        self.scene_loader.touch_down(touch.pos, self.ac_scene)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)
        self.scene_loader.touch_move(touch.pos, self.ac_scene)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        self.scene_loader.touch_up(touch.pos, self.ac_scene)
