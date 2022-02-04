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
import random
from kivy.core.audio import SoundLoader
import json

# Window.size = (720*0.5, 1280*0.5)

class Pipe:
    def __init__(self,start, screen_width, screen_height):
        self.start = start
        self.pos = [[start,screen_height*0.35-50],[start,screen_height*0.55+50]]
        self.w = screen_width/7
        self.vel = 200

        #self.images = ["data/images/t.png", "data/images/f.png", "data/images/m.png"]
        self.images = ["data/images/pipe.png", "data/images/pipe.png", "data/images/pipe.png"]

        self.screen_width = screen_width
        self.screen_height = screen_height


    def restart(self):
        self.pos = [[self.start,self.screen_height*0.35-50],[self.start,self.screen_height*0.55+50]]
        self.pipe_up.pos=(self.pos[0][0],0)
        self.pipe_down.pos=(self.pos[1][0],self.pos[1][1])
        self.pipe_up.size=(self.w,self.pos[0][1])
        self.pipe_down.size=(self.w,self.screen_height-self.pos[1][1])

    def get_x(self):
        return self.pipe_up.pos[0]

    def collide(self,r):

        rect = {"x": r.pos[0], "y": r.pos[1], "width": r.size[0], "height": r.size[1]}
        pipe_up = {"x": self.pipe_up.pos[0], "y": self.pipe_up.pos[1], "width": self.pipe_up.size[0], "height": self.pipe_up.size[1]}
        pipe_down = {"x": self.pipe_down.pos[0], "y": self.pipe_down.pos[1], "width": self.pipe_down.size[0], "height": self.pipe_down.size[1]}

        if ((rect["x"] < pipe_up["x"] + pipe_up["width"] and rect["x"] + rect["width"] > pipe_up["x"] and
            rect["y"] < pipe_up["y"] + pipe_up["height"] and rect["y"] + rect["height"] > pipe_up["y"]) or
            (rect["x"] < pipe_down["x"] + pipe_down["width"] and rect["x"] + rect["width"] > pipe_down["x"] and
            rect["y"] < pipe_down["y"] + pipe_down["height"] and rect["y"] + rect["height"] > pipe_down["y"])):
            return True

    def createPipes(self):
        min_x = int(self.screen_height*0.2)
        max_x = int(self.screen_height*0.8)
        x = random.randint(min_x, max_x)

        self.pos = [[self.screen_width+self.w,x-150],[self.screen_width+self.w,x+150]]
        img = self.images[random.randint(0,2)]

        self.pipe_up.source = img
        self.pipe_down.source = img

        self.pipe_up.pos = (self.pos[0][0],0)
        self.pipe_down.pos = (self.pos[1][0],self.pos[1][1])

        self.pipe_down.size = (self.w,self.screen_height-self.pos[1][1])
        self.pipe_up.size = (self.w,self.pos[0][1])

    def draw(self):
        img = self.images[random.randint(0,2)]
        self.pipe_up = Rectangle(source=img,pos=(self.pos[0][0],0), size=(self.w,self.pos[0][1]))
        self.pipe_down = Rectangle(source=img,pos=(self.pos[1][0],self.pos[1][1]), size=(self.w,self.screen_height-self.pos[1][1]))

    def update(self, dt):
        self.pos[0][0] -= self.vel*dt
        self.pos[1][0] -= self.vel*dt

        self.pipe_up.pos=(self.pos[0][0],0)
        self.pipe_down.pos=(self.pos[1][0],self.pos[1][1])

        if self.pos[0][0] < 0-self.w:
            self.createPipes()


class Bird:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width*0.4
        self.r = screen_width/10

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.img = "data/images/bird.png"

        self.gravity = 60
        self.vel = 0
        self.lift = -20

        self.dead = False

    def restart(self):
        if self.dead:
            self.rect.pos = (self.x,self.screen_height*0.3)
            self.vel = 0
            self.dead = False

    def bounds(self):
        return self.rect

    def up(self):
        if self.dead != True:
            self.vel += self.lift

    def get_x(self):
        return self.rect.pos[0]

    def die(self):
        self.dead = True

    def draw(self):
        self.rect = Rectangle(source=self.img,pos=(self.x,self.screen_height*0.3), size=(self.r, self.r))

    def update(self,dt):
        self.vel += self.gravity*dt
        self.vel *= 0.9

        y = self.rect.pos[1]

        if self.dead != True:
            y -= self.vel
            self.rect.pos = (self.x, y)

        if y > self.screen_height-(self.rect.size[1]/2):
            y = self.screen_height-(self.rect.size[1]/2)
            self.vel = 0
            self.dead = True
        if y < 0:
            self.dead = True
            y = 0
            self.vel = 0


class GameWindow(Screen):
    dead = ObjectProperty(None)
    score_t = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ready = 0
        self.i = False
        self.score = 0

        self.screen_width = Window.size[0]
        self.screen_height = Window.size[1]

        self.b = Bird(self.screen_width, self.screen_height)
        self.pipes = [Pipe(self.screen_width*0.1, self.screen_width, self.screen_height), Pipe(self.screen_width*0.7, self.screen_width, self.screen_height)]

        with self.canvas:
            self.draw()

        Clock.schedule_interval(self.update,0)

    def draw(self):
        self.b.draw()

        for i in range(len(self.pipes)):
            self.pipes[i].draw()


    def update(self,dt):
        if self.ready == 1:
            self.b.update(dt)
            for i in range(len(self.pipes)):
                self.pipes[i].update(dt)

                if self.b.dead:
                    self.dead.text = "You Died !"

                else:
                    if self.pipes[i].get_x() >= self.b.get_x()-1.7 and self.pipes[i].get_x() <= self.b.get_x()+1.7:
                        print("score")
                        self.score += 1
                        self.score_t.text = str(self.score)

                    if self.pipes[i].collide(self.b.bounds()):
                        self.b.die()



    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        self.b.up()
        if self.i != True:
            if self.ready == 0:
                self.ready = 1
        self.i = False

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)

    def restart(self):
        self.dead.text = ""
        self.score = 0
        self.score_t.text = str(self.score)
        self.b.restart()
        for i in range(len(self.pipes)):
            self.pipes[i].restart()
        self.ready = 0
        self.i = True


class MenuWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    # 1520 x 720
    MyMainApp().run()
