from .objects import *

class Scene1:
    def __init__(self, screen_size):
        self.screen_size = screen_size

        self.test_obj = Object()

    def update(self):
        self.test_obj.update()

    def touch_down(self, pos):
        print(f"down = {pos}")
        
        self.test_obj.touch_down(pos)

    def touch_move(self, pos):
        print(f"move = {pos}")

    def touch_up(self, pos):
        print(f"up = {pos}")

class Scene2:
    def __init__(self, screen_size):
        self.screen_size = screen_size

    def update(self):
        Rectangle(pos=(100,100))

    def touch_down(self, pos):
        print(f"down = {pos}")

    def touch_move(self, pos):
        print(f"move = {pos}")

    def touch_up(self, pos):
        print(f"up = {pos}")