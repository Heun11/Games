from os import access
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
import json

from .objects import StaticObject

# Menu
class MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        with self.canvas:
            Rectangle(size=(Window.size[0], Window.size[1]),source="data/images/menu_background.png", pos=(0,0))

# Game
class GameScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.screen_size = Window.size
        self.FPS = 30

        with open(f"data/save_file.json") as f:
            self.actual_scene_id = json.load(f)["scene"]

        with open(f"data/scenes/scene_{self.actual_scene_id}.json") as f:
            self.actual_scene = json.load(f)

    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_interval(self.update,1/self.FPS)

    def update(self, dt):
        # UPDATE
        print(dt)

        # DRAW
        self.canvas.clear()
        with self.canvas:
            for i in range(len(self.actual_scene["static_objects_images"])):
                StaticObject(source=self.actual_scene["static_objects_images"][i], 
                            pos=self.actual_scene["static_objects_pos_size"][str(i)]["pos"],
                            size=self.actual_scene["static_objects_pos_size"][str(i)]["size"]).draw()