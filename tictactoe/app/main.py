import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from random import randint

Window.size = (720*0.7, 1280*0.7)

class tile:
    def __init__(self, pos=(1, 1), size=(50, 50), image=""):
        self.pos = pos
        self.size = size
        self.image = "data/"+image+".png"

    def draw(self):
        self.r = Rectangle(source=self.image ,size=(self.size[0]-1, self.size[1]-1), pos=(self.size[0]*self.pos[1], 450+(self.size[1]*self.pos[0])))

    def update(self, image):
        self.r.source = "data/"+image+".png"

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        FPS = 30

        self.images=[["s", "f"],
                     ["m", "t"]]
        self.p_images = {
            1:self.images[0][randint(0, 1)],
            2:self.images[1][randint(0, 1)],
            0:"0"
        }
        self.update_all = False
        self.rects = [[0 for i in range(3)] for j in range(3)]
        self.size_of_blocks = 100
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.player = 1

        with self.canvas:
            self.draw()

        Clock.schedule_interval(self.update,1/FPS)

    def draw(self):
        for i in range(3):
            for j in range(3):
                t = str(self.board[i][j])
                self.rects[i][j] = tile(pos=(i,j), size=(self.size_of_blocks, self.size_of_blocks), image=t)

        for i in range(3):
            for j in range(3):
                self.rects[i][j].draw()


    def update(self, dt):
        if self.update_all:
            for i in range(3):
                for j in range(3):
                    t = self.p_images[self.board[i][j]]
                    self.rects[i][j].update(t)
            self.update_all = False
            self.check()

    def move(self, mouse_pos):
        x = int(mouse_pos[0])
        y = int(mouse_pos[1])

        for i in range(3):
                for j in range(3):
                    if (x < j*self.size_of_blocks  + self.size_of_blocks and
                        x > j*self.size_of_blocks  and

                        y < i*self.size_of_blocks + 450 + self.size_of_blocks and
                        y > i*self.size_of_blocks + 450):

                        if self.board[i][j] == 0:
                            self.board[i][j] = self.player
                            self.change_player()

    def check(self):
        # CHECK WHO WIN
        pass

                        
    def change_player(self):
        if self.player==1:
            self.player=2
        else:
            self.player=1

    def restart(self):
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.p_images = {
            1:self.images[0][randint(0, 1)],
            2:self.images[1][randint(0, 1)],
            0:"0"
        }
        self.update_all = True
        print("restart")

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        self.move(touch.pos)
        self.update_all = True

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)

class MenuWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
