import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from random import randint
from kivy.core.audio import SoundLoader
import json

Window.size = (1280, 720)

class Box:
    def __init__(self, screen_width, screen_height, start):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.x = start
        self.vel = 0.892857142*screen_width

        self.start_pos_x = start
        self.start_pos_y = self.screen_height*0.3

        self.size = (self.screen_height*0.12,self.screen_height*0.12)
        self.pos = (self.x, self.screen_height*0.3)

        # self.images = ["data/images/debili/m.png", "data/images/debili/f.png", "data/images/debili/s.png"]
        self.images = ["data/images/m.png", "data/images/f.png", "data/images/s.png"]
        self.image = self.images[randint(0,2)]

    def restart(self):
        self.rect.pos = (self.start_pos_x, self.start_pos_y)
        self.x = self.start_pos_x

    def bounds(self):
        return self.rect

    def get_x(self):
        return self.rect.pos[0]

    def update(self, dt):
        self.x -= self.vel*dt

        if self.x < 0-self.size[1]:
            self.x = self.screen_width
            self.image = self.images[randint(0,2)]
            self.rect.source = self.image

        self.rect.pos = (self.x, self.screen_height*0.3)

    def draw(self):
        self.rect = Rectangle(source=self.image, size=self.size, pos=self.pos)

class Dino:
    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.y = self.screen_height*0.3

        self.start_pos_x = self.screen_width*0.3
        self.start_pos_y = self.screen_height*0.3

        self.size = (self.screen_height*0.2,self.screen_height*0.2)
        self.pos = (self.screen_width*0.3, self.y)

        # self.image = "data/images/debili/t.png"
        self.image = "data/images/t.png"
        self.dead = False

        self.is_jump = False
        self.jump_count = 10.5

    def collide(self,r):

        box = {"x": r.pos[0], "y": r.pos[1], "width": r.size[0], "height": r.size[1]}
        rect = {"x": self.rect.pos[0], "y": self.rect.pos[1], "width": self.rect.size[0], "height": self.rect.size[1]}

        if ((box["x"] < rect["x"] + rect["width"] and box["x"] + box["width"] > rect["x"] and
            box["y"] < rect["y"] + rect["height"] and box["y"] + box["height"] > rect["y"])):
            return True

    def restart(self):
        self.rect.pos = (self.start_pos_x, self.start_pos_y)
        self.dead = False

    def die(self):
        self.dead = True

    def get_x(self):
        return self.rect.pos[0]

    def jump(self, bool):
        if self.dead!=True:
            self.is_jump = bool

    def update(self):
        if self.is_jump:
            if self.jump_count >= -10.5:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y += (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10.5

        self.rect.pos = (self.screen_width*0.3, self.y)

    def draw(self):
        self.rect = Rectangle(source=self.image, size=self.size, pos=self.pos)


class GameWindow(Screen):
    dead = ObjectProperty(None)
    score_t = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen_width = Window.size[0]
        self.screen_height = Window.size[1]

        self.ready = 0
        self.i = False
        self.score = 0

        self.dino = Dino(self.screen_width, self.screen_height)
        self.images = ["data/images/m.png", "data/images/f.png", "data/images/s.png"]
        self.boxes = [Box(self.screen_width, self.screen_height, self.screen_width),Box(self.screen_width, self.screen_height, self.screen_width+self.screen_width*0.5)]

        with self.canvas:
            Rectangle(size=(self.screen_width, self.screen_height*0.3), source=self.images[randint(0,2)])
            self.draw()

        Clock.schedule_interval(self.update,0)

    def draw(self):
        self.dino.draw()
        for box in self.boxes:
            box.draw()

    def update(self,dt):
        self.score_t.text = str(self.score)
        if self.ready == 1:
            self.dino.update()
            for box in self.boxes:
                box.update(dt)

                if self.dino.dead:
                    self.dead.text = "Skapal si !"
                else:
                    print(f"{self.screen_width}, {box.vel}, {box.get_x()}, {self.dino.get_x()}")

                    if self.dino.collide(box.bounds()):
                        self.dino.dead = True

                    if box.get_x() >= self.dino.get_x()-13.543762207/2 and box.get_x() <= self.dino.get_x()+13.543762207/2:
                        self.score += 1


    def restart(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                if self.score > data["high_score"]:
                    data["high_score"] = self.score
                    json.dump(data, file, indent=2)
        except:
            with open("data.json", "w") as file:
                data = {"high_score":self.score}
                json.dump(data, file, indent=2)

        self.dead.text = ""
        self.score = 0
        self.dino.restart()
        for box in self.boxes:
            box.restart()
        self.ready = 0
        self.i = True

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        self.dino.jump(True)
        if self.i != True:
            if self.ready == 0:
                self.ready = 1
        self.i = False

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)


class MenuWindow(Screen):
    h_score = ObjectProperty(None)

    def load_h_score(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                return data["high_score"]
        except:
            with open("data.json", "w") as file:
                data = {"high_score":0}
                json.dump(data, file, indent=2)
                return 0

    def load(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                score =  data["high_score"]
        except:
            with open("data.json", "w") as file:
                data = {"high_score":0}
                json.dump(data, file, indent=2)
                score = 0

        self.h_score.text = f"HIGH SCORE: {score}"

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    # 1520 x 720
    MyMainApp().run()
