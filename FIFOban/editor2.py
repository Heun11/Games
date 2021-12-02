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

kv = """
WindowManager:
    MenuWindow:
    EditorWindow:

<Label>:
    background_color: (1,0,0,.5)
    size_hint: 0.3,0.1
    font_size: 40
    color: (0.8,0.8,0.8,1)
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            size: self.size
            pos: self.pos

<Button>:
    size_hint: 0.3,0.1
    font_size: 40
    background_color: (1,1,1,0.01)
    background_color: (0.5,0,0,1)

<TextInput>:
    background_color: (.2,.2,.2,1)
    size_hint: 0.3,0.1
    font_size: 40
    foreground_color:(1,1,1,1)
    multiline:False

<MenuWindow>:
    name: "menu"

    level_width:level_width
    level_height:level_height
    level_name:level_name

    canvas.before:
        Color:
            rgba: 1, 1, 1, 0.05
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "Add parameters:"
        size_hint: 0.3, 0.1
        pos_hint: {"y":0.8, "x":0.35}

    TextInput:
        id: level_name
        hint_text: "name of level"
        pos_hint: {"y":0.6, "x":0.35}
    
    TextInput:
        id: level_width  
        hint_text: "width of level"
        pos_hint: {"y":0.5, "x":0.35}
    
    TextInput:
        id: level_height
        hint_text: "height of level"
        pos_hint: {"y":0.4, "x":0.35}

    Button:
        text: "submit"
        pos_hint: {"y":0.2, "x":0.35}
        on_press:
            root.start_editor()

<EditorWindow>:
    name: "editor"    
"""

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
        self.level = []
        self.block_size = 0

        self.blocks = {"g":0, "p":7, "w":4, "b":2, "c":9, "e":3, 0:"g", 7:"p", 4:"w", 2:"b", 9:"c", 3:"e", 6:""}
        self.actual_block = "g"

        self.save_button = {"pos":[self.sc[0]*0.85-20, self.sc[1]*0.8], "size":[self.sc[0]*0.15, self.sc[1]*0.1], "source":"images/save.png"}
        self.block_buttons = [
            {"pos":[self.sc[0]*0.83, self.sc[1]*0.6], "size":[self.sc[1]*0.08, self.sc[1]*0.08], "source":"images/b.png", "block":"b"},
            {"pos":[self.sc[0]*0.92, self.sc[1]*0.6], "size":[self.sc[1]*0.08, self.sc[1]*0.08], "source":"images/c.png", "block":"c"},
            
            {"pos":[self.sc[0]*0.83, self.sc[1]*0.5], "size":[self.sc[1]*0.08, self.sc[1]*0.08], "source":"images/p.png", "block":"p"},
            {"pos":[self.sc[0]*0.92, self.sc[1]*0.5], "size":[self.sc[1]*0.08, self.sc[1]*0.08], "source":"images/e.png", "block":"e"},

            {"pos":[self.sc[0]*0.83, self.sc[1]*0.4], "size":[self.sc[1]*0.08, self.sc[1]*0.08], "source":"images/w.png", "block":"w"},
            {"pos":[self.sc[0]*0.92, self.sc[1]*0.4], "size":[self.sc[1]*0.08, self.sc[1]*0.08], "source":"images/g.png", "block":"g"}
        ]

    def on_enter(self, *args):
        super().on_enter(*args)
        self.level = [[6 for i in range(level["level_width"])] for j in range(level["level_height"])]
        self.block_size = self.sc[1]*(1/(level["level_height"]+6))
        self.level_offset = [self.block_size*2,self.block_size*2]
        self.tiles = [[Tile(self.block_size, [self.level_offset[0]+((self.block_size+1)*j), self.level_offset[1]+((self.block_size+1)*i)]) for i in range(level["level_width"])] for j in range(level["level_height"])]
        self.draw()
        
    def draw(self):
        self.canvas.clear()
        with self.canvas:
            for i in range(len(self.level)):
                for j in range(len(self.level[i])):
                    self.tiles[i][j].draw()

            Color(1,1,1,0.1)
            Rectangle(pos=[self.save_button["pos"][0]-20, 0], size=[self.sc[0]-self.save_button["pos"][0]+20, self.sc[1]])
            Color(1,1,1,1)

            Rectangle(pos=self.save_button["pos"], size=self.save_button["size"], source=self.save_button["source"])

            for btn in self.block_buttons:
                Rectangle(pos=btn["pos"], size=btn["size"], source=btn["source"])

    def save_level(self):
        print("saving...")

        b_pos=[]
        nm = level["level_name"]
        for i in range(level["level_height"]):
                for j in range(level["level_width"]):
                    if self.level[i][j] == self.blocks["p"]:
                        p_pos = [i, j]
                    elif self.level[i][j] == self.blocks["c"]:
                        b_pos.append([i, j])

        with open(f"data/{nm}.json", "w") as f:
            self.level.reverse()
            data = {
                "size":[level["level_height"], level["level_width"]],
                "map":self.level,
                "player_pos": p_pos,
                "box_places": b_pos 
            }
            json.dump(data, f, indent=2)
            self.level.reverse()

    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        self.update_bool=True

        if (touch.pos[0]>self.save_button["pos"][0] and touch.pos[0]<self.save_button["pos"][0]+self.save_button["size"][0] and
        touch.pos[1]>self.save_button["pos"][1] and touch.pos[1]<self.save_button["pos"][1]+self.save_button["size"][1]):
            self.save_level()

        for btn in self.block_buttons:
            if (touch.pos[0]>btn["pos"][0] and touch.pos[0]<btn["pos"][0]+btn["size"][0] and
            touch.pos[1]>btn["pos"][1] and touch.pos[1]<btn["pos"][1]+btn["size"][1]):
                self.actual_block = btn["block"]

        if (touch.pos[0]>self.level_offset[0] and touch.pos[0]<self.level_offset[0]+(self.block_size*len(self.level[0])+len(self.level[0])) and
        touch.pos[1]>self.level_offset[1] and touch.pos[1]<self.level_offset[1]+(self.block_size*len(self.level)+len(self.level))):
            pos = [touch.pos[0]-self.level_offset[0], touch.pos[1]-self.level_offset[1]]
            j, i = math.floor(pos[0]/(self.block_size+1)), math.floor(pos[1]/(self.block_size+1))
            self.level[i][j] = self.blocks[self.actual_block]
            self.tiles[j][i].update(self.actual_block)


class MenuWindow(Screen):
    level_width = ObjectProperty(None)
    level_height = ObjectProperty(None)
    level_name = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def start_editor(self):
        if self.level_height.text=="" or self.level_width.text=="" or self.level_name.text=="":
            level["level_height"] = 10
            level["level_width"] = 10
            level["level_name"] = "debil_lenivy"
        else:
            level["level_height"] = int(self.level_height.text)
            level["level_width"] = int(self.level_width.text)
            level["level_name"] = self.level_name.text

        self.parent.current = "editor"
        self.parent.transition.direction = "up"

class WindowManager(ScreenManager):
    pass

Window.size = (1100, 800)

class EditorApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    EditorApp().run()