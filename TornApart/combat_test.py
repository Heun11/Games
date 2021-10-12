# Game
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty
import random
from kivy.graphics import Rectangle
from kivy.graphics import Color

import lib

# Window.size = (720*0.5, 1280*0.5)

kv_string = """

WindowManager:
    GameWindow:

<Label>:
    background_color: (1,0,0,.5)
    size_hint: 0.3,0.1
    font_size: 40
    color: (0.8,0.8,0.8,1)
    # canvas.before:
    #     Color:
    #         rgba: self.background_color
    #     Rectangle:
    #         size: self.size
    #         pos: self.pos

<Button>:
    size_hint: 0.2,0.1
    font_size: 40
    background_color: (1,1,1,0.01)
    # background_color: (0,0,1,1)

<GameWindow>:
    name: "game"

"""

class Human:
    def __init__(self, size=(50,50), pos=(0,0), source="", p=False):
        self.size = size
        self.pos = pos
        self.source = source
        self.rect = Rectangle(size=self.size,pos=self.pos,source=self.source)
        self.p = p
        self.hp = 10
        if p:
            self.dmg = 5
        else:
            self.dmg = 1

    def get_bounds(self):
        return {"x":self.rect.pos[0],"y":self.rect.pos[1],"w":self.rect.size[0],"h":self.rect.size[1]}

    def get_hp(self):
        return int(self.hp)

    def attack(self, target):
        target.hp -= self.dmg

    def draw(self):
        if self.p:
            Color(0,1,0,1)
        else:
            Color(1,0,0,1)
        self.rect = Rectangle(size=self.size,pos=self.pos,source=self.source)

    def update(self):
        if self.hp < 0:
            self.hp = 0

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        FPS = 60
        Clock.schedule_interval(self.update,1/FPS)

        self.t = 1

        self.player = Human(pos=(100, 300), p=True)
        self.enemies = [Human(pos=(400, 300)), Human(pos=(480, 300))]

    def update(self,dt):
        self.player.update()
        for i in self.enemies:
            i.update()

        self.canvas.clear()
        with self.canvas:
            self.player.draw()
            for i in range(len(self.enemies)):
                self.enemies[i].draw()
                
                Color(0,1,0,1)
                Rectangle(pos=(400, 150+(50*i)),size=(20*self.enemies[i].get_hp(), 20))
            Rectangle(pos=(50, 200),size=(20*self.player.get_hp(), 20))


    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        if self.t == 1:
            m = {"x":touch.pos[0], "y":touch.pos[1]}
            for i in self.enemies:
                if (m["x"]>i.get_bounds()["x"] and m["x"]<(i.get_bounds()["x"]+i.get_bounds()["w"]) and 
                    (m["y"]>i.get_bounds()["y"] and m["y"]<(i.get_bounds()["y"]+i.get_bounds()["h"]))):
                    self.player.attack(i)
                    self.t = 0
        else:
            for i in self.enemies:
                i.attack(self.player)

            self.t = 1

    def on_touch_up(self, touch):
        super().on_touch_up(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_string(kv_string)

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
