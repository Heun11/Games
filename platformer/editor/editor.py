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
    "level_width":None,
    "level_height":None,
    "level_name":None
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
        

class MenuWindow(Screen):
    level_width = ObjectProperty(None)
    level_height = ObjectProperty(None)
    level_name = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def start_editor(self):
        if self.level_name.text=="":
            if self.level_height.text=="" or self.level_width.text=="":
                level["level_height"] = 10
                level["level_width"] = 10
                level["level_name"] = "debil_lenivy"
            else:
                level["level_height"] = int(self.level_height.text)
                level["level_width"] = int(self.level_width.text)
                level["level_name"] = "debil"
        else:
            level["level_height"] = int(self.level_height.text)
            level["level_width"] = int(self.level_width.text)
            level["level_name"] = self.level_name.text

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