from kivy.core.window import Window
from .objects import Object
import json

class SceneLoader:
    def __init__(self):
        with open(f"data/save_file.json") as f:
            self.actual_scene_id = json.load(f)["scene"]

        self.scenes = [0,Scene1(),2,3,4,5]

    def update_draw(self):
        self.scenes[self.actual_scene_id].update_draw()

    def touch(self, touch, type):
        if type == "down":  
            print(f"down = {touch.pos}")

        elif type == "up":  
            print(f"up = {touch.pos}")

        elif type == "move":  
            print(f"move = {touch.pos}")


class Scene1:
    def __init__(self):
        pass

    def update_draw(self):
        Object().update_draw()