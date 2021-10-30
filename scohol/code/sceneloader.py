from .objects import *
from .classes import *

class SceneLoader:
    def __init__(self, screen_size, player=None):
        self.player = player
        self.screen_size = screen_size
        self.scenes = {
            1:{
                "objects":[Object(size=[200,200], pos=[300,200])],
                "player":Player(size=(100,100), pos=(100,100), source="", movable_space={"x":[100,900], "y":[10,600]})
            }
        }

    def update(self, scene_id):
        Rectangle(size=(self.screen_size[0], self.screen_size[1]),source=f"data/images/background{scene_id}.png", pos=(0,0))
        for i in self.scenes[scene_id]["objects"]:
            i.draw()

        self.scenes[scene_id]["player"].draw()

    def get_pressed(self, scene_id, touch_pos):
        for i in self.scenes[scene_id]["objects"]:
            i.pressed(touch_pos)

        self.scenes[scene_id]["player"].pressed(touch_pos)