from .objects import *

from kivy.graphics import Color

class Scene1:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        # self.objects = [Picture(pos=[400, 470], source="data/images/picture1.png", size=[120,120]), Computer(pos=[620, 435], size=[130,130]), 
        #                 Door(pos=[885, 180], size=[150, 300], scene=2, source="data/images/door1.png")]
        self.objects = [Picture(pos=[0.3, 0.6], source="data/images/picture1.png", size=[0.11,0.14], screen_size=self.screen_size), 
                        Computer(pos=[0.48, 0.58], size=[0.11,0.14], screen_size=self.screen_size), 
                        Door(pos=[0.67, 0.29], size=[0.11, 0.38], scene=2, source="data/images/door1.png", screen_size=self.screen_size)]
        # self.movable_space = [[350,screen_size[0]-360],[100,300]]
        self.movable_space = [[screen_size[0]*0.25, screen_size[0]*0.7], [screen_size[1]*0.14, screen_size[1]*0.33]]
        self.player = Player(ms=self.movable_space, pos=[0.1,0.1], size=[0.06, 0.1],screen_size=self.screen_size)
        self.background = Background(source="data/images/pozadie1.png", size=self.screen_size)

    def update(self):
        self.background.update()

        # MOVABLE SPACE VISIBLE
        # Color(1,0,0,1)
        # Rectangle(size=(self.movable_space[0][1]-self.movable_space[0][0], self.movable_space[1][1]-self.movable_space[1][0]), 
        #           pos=(self.movable_space[0][0], self.movable_space[1][0]))
        # Color(1,1,1,1)
        #=====================

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