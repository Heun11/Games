import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from functools import partial

import json

Window.size = (720*0.7, 1280*0.7)

def load_level(index):
    try:
        with open("data/levels.json") as f:
            levels = json.load(f)
        return levels[str(index)]
    except Exception as e:
        print("error loading levels", e)

class GamePad:
    def __init__(self, screen_size, player):
        self.source="data/images/gamepad.png"
        self.size=screen_size[0]*0.3
        self.pos=[screen_size[0]*0.35, screen_size[1]*0.2]
        self.player=player

    def update(self):
        Rectangle(source=self.source, pos=self.pos, size=[self.size, self.size])

    def on_touch(self, touch):
        pos=touch.pos
        size_of_btn=self.size/3

        if ((pos[0] > self.pos[0]+size_of_btn) and (pos[0] < self.pos[0]+size_of_btn*2) and
            (pos[1] > self.pos[1]+size_of_btn*2) and (pos[1] < self.pos[1]+self.size)):
            print("up")
            self.player.move(0)

        if ((pos[0] > self.pos[0]+size_of_btn) and (pos[0] < self.pos[0]+size_of_btn*2) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+size_of_btn)):
            print("down")
            self.player.move(1)

        if ((pos[0] > self.pos[0]+size_of_btn*2) and (pos[0] < self.pos[0]+self.size) and
            (pos[1] > self.pos[1]+size_of_btn) and (pos[1] < self.pos[1]+size_of_btn*2)):
            print("right")
            self.player.move(2)

        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+size_of_btn) and
            (pos[1] > self.pos[1]+size_of_btn) and (pos[1] < self.pos[1]+size_of_btn*2)):
            print("left")
            self.player.move(3)

class tile:
    def __init__(self, pos=(1, 1), size=(50, 50), image=""):
        self.pos = pos
        self.size = size
        self.image = "data/images/"+image+".png"

    def draw(self):
        self.r = Rectangle(source=self.image ,size=self.size, pos=(self.size[0]*self.pos[1], 450+(self.size[1]*self.pos[0])))

    def update(self, image):
        self.r.source = "data/images/"+image+".png"

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.level_id = 0
        self.level = load_level(self.level_id)
        self.level["map"].reverse()
        self.blocks = {"g":0, "p":7, "w":4, "b":2, "c":9, "e":3}
        self.rects = [[0 for i in range(self.level["size"][1])] for j in range(self.level["size"][0])]

        Clock.schedule_interval(self.update,1/60)


    def update(self, dt):
        self.clear_widgets()
        self.canvas.clear()
        
        self.add_widget(Button(text="a", pos_hint={"x":0.2, "y":0.15}, size_hint=(0.2,0.1), on_press=partial(self.move, "a", -1, 0)))
        self.add_widget(Button(text="d", pos_hint={"x":0.6, "y":0.15}, size_hint=(0.2,0.1), on_press=partial(self.move, "d", 1, 0)))
        self.add_widget(Button(text="w", pos_hint={"x":0.4, "y":0.25}, size_hint=(0.2,0.1), on_press=partial(self.move, "w", 0, 1)))
        self.add_widget(Button(text="s", pos_hint={"x":0.4, "y":0.05}, size_hint=(0.2,0.1), on_press=partial(self.move, "s", 0, -1)))

        print(1/dt)
        with self.canvas:
            for i in range(self.level["size"][0]):
                for j in range(self.level["size"][1]):

                    if self.level["map"][i][j] == self.blocks["g"]:
                        t = "g"
                    elif self.level["map"][i][j] == self.blocks["p"]:
                        t = "p"
                    elif self.level["map"][i][j] == self.blocks["w"]:
                        t = "w"
                    elif self.level["map"][i][j] == self.blocks["b"]:
                        t = "b"
                    elif self.level["map"][i][j] == self.blocks["c"]:
                        t = "c"
                    elif self.level["map"][i][j] == self.blocks["e"]:
                        t = "e"

                    self.rects[i][j] = tile(pos=(i,j), size=(40, 40), image=t)

            for i in range(self.level["size"][0]):
                for j in range(self.level["size"][1]):
                    self.rects[i][j].draw()

    def check(self):
        pass   

    def get_obj(self, x, y):
        pl_pos = self.level["player_pos"]
        level = self.level["map"]
        obj = level[pl_pos[0]+y][pl_pos[1]+x]
        return obj

    def move_all(self, x, y, box_pos=[0, 0], box=False):
        pl_pos = self.level["player_pos"]
        box_places = self.level["box_places"]
        level = self.level["map"]

        if box:
            level[pl_pos[0]+box_pos[1]][pl_pos[1]+box_pos[0]] = self.blocks["b"]

        level[pl_pos[0]][pl_pos[1]] = self.blocks["g"]
        level[pl_pos[0]+y][pl_pos[1]+x] = self.blocks["p"]
        self.level["player_pos"] = [pl_pos[0]+y, pl_pos[1]+x]

        for box_place in box_places:
            if (level[box_place[0]][box_place[1]] == self.blocks["b"]) or (level[box_place[0]][box_place[1]] == self.blocks["p"]):
                pass
            else:
                level[box_place[0]][box_place[1]] = self.blocks["c"]

    def move(self, dr, x, y, *a):
        obj = self.get_obj(x, y)

        if obj == self.blocks["g"] or obj == self.blocks["c"]:
            self.move_all(x, y)

        elif obj == self.blocks["b"]:

            if dr == "a":
                if self.get_obj(-2, 0) == self.blocks["g"] or self.get_obj(-2, 0) == self.blocks["c"]:
                    self.move_all(-1, 0, box=True, box_pos=[-2, 0])

            elif dr == "d":
                if self.get_obj(2, 0) == self.blocks["g"] or self.get_obj(2, 0) == self.blocks["c"]:
                    self.move_all(1, 0, box=True, box_pos=[2, 0])

            elif dr == "w":
                if self.get_obj(0, 2) == self.blocks["g"] or self.get_obj(0, 2) == self.blocks["c"]:
                    self.move_all(0, 1, box=True, box_pos=[0, 2])
            
            elif dr == "s":
                if self.get_obj(0, -2) == self.blocks["g"] or self.get_obj(0, -2) == self.blocks["c"]:
                    self.move_all(0, -1, box=True, box_pos=[0, -2])

        self.update_all = True

    def restart(self):
        self.level = load_level(self.level_id)
        self.level["map"].reverse()
        self.update_all = True
        print("restart")

class MenuWindow(Screen):
    pass

class LevelWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
