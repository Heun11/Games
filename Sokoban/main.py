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

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Window.size = (720*0.7, 1280*0.7)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def load_level(index):
    try:
        with open("data/levels.json") as f:
            levels = json.load(f)
        return levels[str(index)]
    except Exception as e:
        print("error loading levels", e)

def get_save_data():
    try:
        with open("data/save.json") as f:
            d = json.load(f)
            return [d["index_of_actual_level"], d["maximum_level"]]
    except Exception as e:
        print("error loading data", e)

def save_data(index, max_):
    try:
        with open("data/save.json", "w") as f:
            d = {
                "index_of_actual_level":index,
                "maximum_level":max_
            }
            json.dump(d, f, indent=2)
    except Exception as e:
        print("error saving data", e) 

level_index = 1
SOUNDS = {
    "btn":SoundLoader.load("data/sounds/debili/btn.wav"),
    "restart":SoundLoader.load("data/sounds/debili/restart.wav"),
    "win":SoundLoader.load("data/sounds/debili/win.wav"),
    "step":SoundLoader.load("data/sounds/debili/step.wav")
}

class GamePad:
    def __init__(self, sc, par=None):
        self.source="data/images/gamepad.png"
        self.size=sc[0]*0.5
        self.pos=[sc[0]*0.25, sc[1]*0.1]
        self.par=par

    def update(self):
        Rectangle(source=self.source, pos=self.pos, size=[self.size, self.size])

    def on_touch(self, touch):
        pos=touch.pos
        size_of_btn=self.size/3

        if ((pos[0] > self.pos[0]+size_of_btn) and (pos[0] < self.pos[0]+size_of_btn*2) and
            (pos[1] > self.pos[1]+size_of_btn*2) and (pos[1] < self.pos[1]+self.size)):
            self.par.move("w",0,1)

        if ((pos[0] > self.pos[0]+size_of_btn) and (pos[0] < self.pos[0]+size_of_btn*2) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+size_of_btn)):
            self.par.move("s",0,-1)

        if ((pos[0] > self.pos[0]+size_of_btn*2) and (pos[0] < self.pos[0]+self.size) and
            (pos[1] > self.pos[1]+size_of_btn) and (pos[1] < self.pos[1]+size_of_btn*2)):
            self.par.move("d",1,0)

        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+size_of_btn) and
            (pos[1] > self.pos[1]+size_of_btn) and (pos[1] < self.pos[1]+size_of_btn*2)):
            self.par.move("a",-1,0)

class GameWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sc = Window.size
        self.update_all = False

        self.level_id, self.max_level = level_index, get_save_data()[1]
        self.level = load_level(self.level_id)
        self.level["map"].reverse()

        self.blocks = {"g":0, "p":7, "w":4, "b":2, "c":9, "e":3}
        self.gp = GamePad(sc=self.sc, par=self)

        self.button = {"pos":(0, self.sc[1]*0.95), "size":(self.sc[0]*0.1, self.sc[1]*0.05), "source":"data/images/button.png"}
        self.button__menu_content = BoxLayout(orientation='vertical')
        self.button__menu_content.add_widget(Button(text="restart", size_hint=(1, 0.5), on_press=self.restart))
        self.button__menu_content.add_widget(Button(text="menu",size_hint=(1, 0.5), on_press=self.menu))
        self.button_menu = Popup(title='Options:',content=self.button__menu_content, size_hint=(0.6,0.4))

        Clock.schedule_interval(self.update,1/30)

    def on_enter(self, *args):
        super().on_enter(*args)
        self.level_id=level_index
        self.set_level()
        self.update_all = True

    def update(self, dt):
        if self.update_all:

            self.clear_widgets()
            self.canvas.clear()

            # print(1/dt)
            with self.canvas:
                for i in range(self.level["size"][0]):
                    for j in range(self.level["size"][1]):
                        if self.level["map"][i][j] != self.blocks["e"]:

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

                            source = f"data/images/{t}.png"
                            # source = f"data/images/debili/{t}.png"

                            Rectangle(source=source, size=self.tile_size, 
                                        pos=[self.tile_offset[0]+self.tile_size[0]*j, self.tile_offset[1]+self.tile_size[1]*i])

                Rectangle(pos=self.button["pos"], size=self.button["size"], source=self.button["source"])
                self.gp.update()

                if self.check():
                    SOUNDS["win"].play()
                    if self.level_id<self.max_level:
                        self.level_id+=1
                        self.set_level()
                        if get_save_data()[0]<self.max_level and self.level_id>get_save_data()[0]:
                            save_data(self.level_id, self.max_level)
                    else:
                        self.menu()

    def check(self):
        box_right_count = 0
        box_places = self.level["box_places"]
        level = self.level["map"]

        for b_p in box_places:
            if level[b_p[0]][b_p[1]]==self.blocks["b"]:
                box_right_count+=1
        
        if box_right_count==(len(box_places)):
            return True
        return False

    def set_level(self):
        self.level = load_level(self.level_id)
        self.level["map"].reverse()
        if self.level["size"][0]>self.level["size"][1]:
            self.tile_size = [
                self.sc[0]*(1/(self.level["size"][0]+2)),
                self.sc[0]*(1/(self.level["size"][0]+2))
            ]
        else:
            self.tile_size = [
                self.sc[0]*(1/(self.level["size"][1]+2)),
                self.sc[0]*(1/(self.level["size"][1]+2))
            ]
        self.tile_offset = [
            (self.sc[0]*0.5)-((self.level["size"][1])*self.tile_size[0])*0.5,
            self.sc[1]*0.4+((self.sc[1]*0.6)*0.5)-(self.level["size"][0]*self.tile_size[1])*0.5
        ]
        
    def get_obj(self, x, y):
        pl_pos = self.level["player_pos"]
        return self.level["map"][pl_pos[0]+y][pl_pos[1]+x]

    def move_all(self, x, y, box_pos=[0, 0], box=False):
        pl_pos = self.level["player_pos"]
        box_places = self.level["box_places"]
        level = self.level["map"]

        if box:
            level[pl_pos[0]+box_pos[1]][pl_pos[1]+box_pos[0]] = self.blocks["b"]

        level[pl_pos[0]][pl_pos[1]] = self.blocks["g"]
        level[pl_pos[0]+y][pl_pos[1]+x] = self.blocks["p"]
        self.level["player_pos"] = [pl_pos[0]+y, pl_pos[1]+x]

        SOUNDS["step"].play()

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

    def restart(self, *a):
        self.button_menu.dismiss()
        self.level = load_level(self.level_id)
        self.level["map"].reverse()
        SOUNDS["btn"].play()

    def menu(self, *a):
        self.button_menu.dismiss()
        self.parent.current = "menu"
        self.update_all=False
        self.restart()
        SOUNDS["btn"].play()

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        self.gp.on_touch(touch=touch)

        if ((touch.pos[0]>self.button["pos"][0] and touch.pos[0]<self.button["pos"][0]+self.button["size"][0]) and
        (touch.pos[1]>self.button["pos"][1] and touch.pos[1]<self.button["pos"][1]+self.button["size"][1])):
            self.button_menu.open()
            SOUNDS["btn"].play()

class LevelWindow(Screen):
    levels_layout = ObjectProperty(None)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.sc = Window.size

    def on_enter(self):
        self.levels_layout.clear_widgets()
        unlocked_level, level_count = get_save_data()
        for level_index in range(level_count):
            if level_index+1>unlocked_level:
                l = "Locked"
            else:
                l = "Unlocked"
            self.levels_layout.add_widget(Button(font_size=self.sc[0]//18,text=f"Level:{level_index+1}\n{l}", 
                                                on_press=partial(self.play_level, level_index+1, l)))

    def play_level(self, li, l, *a):
        if l == "Unlocked":
            global level_index
            self.parent.current="game"
            level_index=li

            self.play_music()
    
    def play_music(self):
        SOUNDS["btn"].play()

class MenuWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def play_music(self):
        SOUNDS["btn"].play()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
