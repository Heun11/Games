from .objects import *

from kivy.graphics import Color

class Scene1:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.objects = [Picture(pos=[400, 500]), Computer(pos=[600, 350]), Door(pos=[1000, 150], size=[150, 300], scene=2)]
        self.movable_space = [[100,screen_size[0]-100],[10,300]]
        self.player = Player(ms=self.movable_space)

    def update(self):
        # MOVABLE SPACE VISIBLE
        Color(1,0,0,1)
        Rectangle(size=(self.movable_space[0][1]-self.movable_space[0][0], self.movable_space[1][1]-self.movable_space[1][0]), 
                  pos=(self.movable_space[0][0], self.movable_space[1][0]))
        Color(1,1,1,1)

        for i in self.objects:
            i.update()

        self.player.update()

    def touch_down(self, pos):
        for i in self.objects:
            i.touch_down(pos)

        self.player.touch_down(pos)

    def touch_move(self, pos):
        pass

    def touch_up(self, pos):
        pass

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