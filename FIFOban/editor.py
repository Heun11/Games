import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.uix.button import Button
import json

width = int(input("width of level: "))
height = int(input("height of level: "))
name = input("name: ")
mapa = [[6 for i in range(width)] for j in range(height)]

level_parameters = {
    "name":name,
    "size":[height, width],
    "map": mapa,
    "player_pos": [],
    "box_places": [] 
}

class tile:
    def __init__(self, pos=(1, 1), size=(50, 50), image=""):
        self.pos = pos
        self.size = size
        self.image = "data/images/"+image+".png"

    def draw(self):
        self.r = Rectangle(source=self.image ,size=(self.size[0]-1, self.size[1]-1), pos=(100+self.size[0]*self.pos[1], (200+self.size[1]*self.pos[0])))

    def update(self, image):
        self.r.source = "data/images/"+image+".png"

class editor(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        FPS = 30

        self.blocks = {"g":0, "p":7, "w":4, "b":2, "c":9, "e":3}
        self.rects = [[0 for i in range(level_parameters["size"][1])] for j in range(level_parameters["size"][0])]
        self.update_all = False
        self.actual_block = "g"

        self.size_of_blocks = 40

        with self.canvas:
            self.draw()

        Clock.schedule_interval(self.update,1/FPS)

    def draw(self):
        print("ok")

        for i in range(level_parameters["size"][0]):
            for j in range(level_parameters["size"][1]):
                t = ""
                if level_parameters["map"][i][j] == self.blocks["g"]:
                    t = "g"
                elif level_parameters["map"][i][j] == self.blocks["p"]:
                    t = "p"
                elif level_parameters["map"][i][j] == self.blocks["w"]:
                    t = "w"
                elif level_parameters["map"][i][j] == self.blocks["b"]:
                    t = "b"
                elif level_parameters["map"][i][j] == self.blocks["c"]:
                    t = "c"
                elif level_parameters["map"][i][j] == self.blocks["e"]:
                    t = "e"

                self.rects[i][j] = tile(pos=(i,j), size=(self.size_of_blocks, self.size_of_blocks), image=t)

        for i in range(level_parameters["size"][0]):
            for j in range(level_parameters["size"][1]):
                self.rects[i][j].draw()

    def update(self, dt):
        if self.update_all:
            for i in range(level_parameters["size"][0]):
                for j in range(level_parameters["size"][1]):
                    t = ""
                    if level_parameters["map"][i][j] == self.blocks["g"]:
                        t = "g"
                    elif level_parameters["map"][i][j] == self.blocks["p"]:
                        t = "p"
                    elif level_parameters["map"][i][j] == self.blocks["w"]:
                        t = "w"
                    elif level_parameters["map"][i][j] == self.blocks["b"]:
                        t = "b"
                    elif level_parameters["map"][i][j] == self.blocks["c"]:
                        t = "c"
                    elif level_parameters["map"][i][j] == self.blocks["e"]:
                        t = "e"
                    self.rects[i][j].update(t)
            self.update_all = False

    def set_block(self, obj):
        self.actual_block = obj

    def place_block(self, mouse_pos):
        x = int(mouse_pos[0])
        y = int(mouse_pos[1])

        # print(f"block placed on x:{x}, y:{y}")

        for i in range(level_parameters["size"][0]):
                for j in range(level_parameters["size"][1]):
                    if (x < j*self.size_of_blocks + 100 + self.size_of_blocks and
                        x > j*self.size_of_blocks + 100 and

                        y < i*self.size_of_blocks + 200 + self.size_of_blocks and
                        y > i*self.size_of_blocks + 200):

                        t = self.blocks[self.actual_block]
                        level_parameters["map"][i][j] = t

    def save(self):
        nm = level_parameters["name"]
        for i in range(level_parameters["size"][0]):
                for j in range(level_parameters["size"][1]):
                    if level_parameters["map"][i][j] == self.blocks["p"]:
                        level_parameters["player_pos"] = [i, j]
                    elif level_parameters["map"][i][j] == self.blocks["c"]:
                        level_parameters["box_places"].append([i, j])

        with open(f"data/{nm}.json", "w") as f:
            level_parameters["map"].reverse()
            json.dump(level_parameters, f, indent=2)
            level_parameters["map"].reverse()

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

        self.place_block(touch.pos)
        self.update_all = True

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)

class EditorApp(App):
    def build(self):
        return editor()


if __name__ == "__main__":
    EditorApp().run()