from .scenes import *

class SceneLoader:
    def __init__(self, screen_size):
        self.scenes = {1:Scene1(screen_size), 2:Scene2(screen_size)}

    def update(self, scene_id):
        self.scenes[scene_id].update()

    def touch_down(self, pos, scene_id):
        self.scenes[scene_id].touch_down(pos)

    def touch_move(self, pos, scene_id):
        self.scenes[scene_id].touch_move(pos)

    def touch_up(self, pos, scene_id):
        self.scenes[scene_id].touch_up(pos)