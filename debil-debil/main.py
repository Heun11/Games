import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from functools import partial
import json
from random import randint

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Window.size = (720*0.7, 1280*0.7)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# TODO  -> Spravit falling sand simulation:
#       -> treba reversnut self.sand aby 0,0 bolo v lavo hore
#       -> treba dobre spravit ten sand fall
#       -> SPEED IT UP

class Sand:
    def __init__(self, s_size, pos, num):
        self.s_size = s_size
        self.num = num
        self.sand_c = 0
        self.size = s_size[0]/100
        self.height = int(self.s_size[1]/self.size)
        self.width = 100
        self.sand = [[0 for i in range(self.width)] for j in range(self.height)]

        self.pos = self.reverse_pos(pos)
        self.sand_poss = []

    def create_wall(self, pos, size):
        pos = self.reverse_pos(pos)
        for i in range(size[0]):
            for j in range(size[1]):
                if pos[0]>=0 and pos[0]<=self.width-1 and pos[1]>=0 and pos[1]<=self.height-1:
                    self.sand[pos[1]+j][pos[0]+i] = 2
                    self.sand_r[pos[1]+j][pos[0]+i].source = "data/images/wall.png"

    def reverse_pos(self, pos):
        return [pos[0], self.height-pos[1]]

    def draw(self):
        self.sand_r = [[Rectangle(source="data/images/back.png", size=[self.size, self.size], pos=[self.size*i, self.size*j]) for i in range(self.width)] for j in range(self.height)]

    def update(self):
        self.sand = [[0 for i in range(self.width)] for j in range(self.height)]
        if self.sand_c < self.num:
            self.sand_c+=1
            self.sand[self.pos[1]][self.pos[0]] = 1
            self.sand_poss.append(self.pos)

        self.create_wall([0,100], [20,10])

        for i in range(len(self.sand_poss)):
            if self.sand_poss[i][1]>0:
                if self.sand[self.sand_poss[i][1]-1][self.sand_poss[i][0]] == 0:
                    self.sand_r[self.sand_poss[i][1]][self.sand_poss[i][0]].source = "data/images/back.png"
                    self.sand_poss[i] = [self.sand_poss[i][0], self.sand_poss[i][1]-1]

                elif self.sand_poss[i][0]>0 and self.sand[self.sand_poss[i][1]-1][self.sand_poss[i][0]-1] == 0:
                    self.sand_r[self.sand_poss[i][1]][self.sand_poss[i][0]].source = "data/images/back.png"
                    self.sand_poss[i] = [self.sand_poss[i][0]-1, self.sand_poss[i][1]-1]

                elif self.sand_poss[i][0]<self.width-1 and self.sand[self.sand_poss[i][1]-1][self.sand_poss[i][0]+1] == 0:
                    self.sand_r[self.sand_poss[i][1]][self.sand_poss[i][0]].source = "data/images/back.png"
                    self.sand_poss[i] = [self.sand_poss[i][0]+1, self.sand_poss[i][1]-1]

            self.sand[self.sand_poss[i][1]][self.sand_poss[i][0]] = 1
            self.sand_r[self.sand_poss[i][1]][self.sand_poss[i][0]].source = "data/images/sand.png"

# class Sand:
#     def __init__(self, size, pos, speed):
#         self.size = size
#         self.pos = pos
#         self.speed = speed

#     def draw(self):
#         self.rect = Rectangle(pos=self.pos, size=[self.size, self.size], source="data/images/sand.png")

#     def update(self, dt):
#         x_off = randint(-3, 3)
#         self.rect.pos = [self.rect.pos[0]+x_off, self.rect.pos[1]-self.speed]

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_size = Window.size
        self.ready = False

        # sand = {
        #     "size":5,
        #     "pos":[self.screen_size[0]/2,self.screen_size[1]-10],
        #     "speed":5
        # }
        # self.sand = []
        # for i in range(100):
        #     self.sand.append(Sand(sand["size"], sand["pos"], sand["speed"]))

        # self.sand_c = 0
        # self.frame_c = 0
        
        self.sand = Sand(self.screen_size, [10, 10], 200)

        with self.canvas:
            self.draw()

        Clock.schedule_interval(self.update, 1/30)

    def on_enter(self):
        self.ready = True

    def draw(self):
        # for i in self.sand:
        #     i.draw()
        
        self.sand.draw()

    def update(self, dt):
        if self.ready:
        #     if self.sand_c<100:
        #         self.frame_c += 1
        #         if self.frame_c%3==0:
        #             self.sand_c+=1
        #     for i in range(self.sand_c):
        #         self.sand[i].update(dt)
        
            self.sand.update()
        print(1/dt)

class MenuWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
