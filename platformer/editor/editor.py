import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.uix.button import Button
import json, math

level = {
    "width":None,
    "height":None,
    "name":None
}

def print_level(level):
    print()
    for i in range(len(level)):
        for j in range(len(level[i])):
            print(f"{level[i][j]}", end=" ")
        print()

class Tile:
    def __init__(self, size, pos):
        self.size = size
        self.pos = pos

    def draw(self):
        self.r = Rectangle(size=[self.size, self.size], pos=self.pos, source="")

    def update(self, block):
        self.r.source=f"images/{block}.png"

class EditorWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sc = Window.size
    
        self.level = []
        self.blocks = []
        self.selected_block = None

        self.save_button = Button(text="save", size_hint=[0.2,0.1], pos_hint={"x":0.8, "y":0.9}, on_press=self.save_level)

    def on_enter(self, *args):
        super().on_enter(*args)
        self.level = [[6 for i in range(level["width"])] for j in range(level["height"])]
        if level["width"]>level["height"]:
            self.block_size = (self.sc[0]*0.8)*(1/(level["width"]+4))
        else:
            self.block_size = self.sc[1]*(1/(level["height"]+4))
        print(self.block_size)
        self.level_offset = [self.block_size*2,self.block_size*2]
        self.tiles = [[Tile(self.block_size-1, [self.level_offset[0]+(self.block_size*i), self.level_offset[1]+(self.block_size*j)]) for i in range(level["width"])] for j in range(level["height"])]
        self.draw()

    def draw(self):
        with self.canvas:
            Color(1,1,1,0.1)
            Rectangle(pos=[0, 0], size=[self.sc[0]*0.8, self.sc[1]])
            Color(1,1,1,1)
            for i in range(len(self.level)):
                for j in range(len(self.level[i])):
                    self.tiles[i][j].draw()


        self.add_widget(self.save_button)

    def save_level(self, *args):
        print("saving...")

class MenuWindow(Screen):
    level_width = ObjectProperty(None)
    level_height = ObjectProperty(None)
    level_name = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def start_editor(self):
        if self.level_name.text=="":
            if self.level_height.text=="" or self.level_width.text=="":
                level["height"] = 10
                level["width"] = 10
                level["name"] = "debil_lenivy"
            else:
                level["height"] = int(self.level_height.text)
                level["width"] = int(self.level_width.text)
                level["name"] = "debil"
        else:
            level["height"] = int(self.level_height.text)
            level["width"] = int(self.level_width.text)
            level["name"] = self.level_name.text

        self.parent.current = "editor"
        self.parent.transition.direction = "up"

class WindowManager(ScreenManager):
    pass

Window.size = (1100, 800)
kv = Builder.load_file("editor.kv")

class EditorApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    EditorApp().run()