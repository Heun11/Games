from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.clock import Clock
import json

def load_level(index):
    try:
        with open(f"data/levels/{index}.json") as f:
            data = json.load(f)
            for i in range(2):
                data[f"map_floor_{i}"].reverse()
                for j in data[f"map_floor_{i}"]:
                    j.reverse()
            return data
    except:
        return [[0]]

class GameScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.FPS = 30
        self.sc = Window.size

        self.level_index = 0
        self.level = load_level(self.level_index)

        self.tile_size = [96*2.5, 48*2.5]
        self.tile_offset = [500, 100]

        self.object_size = [48*1.5, 96*1.5]

    def on_enter(self, *args):
        super().on_enter(*args)
        Clock.schedule_interval(self.update,1/self.FPS)

    def update(self, dt):
        self.canvas.clear()
        self.clear_widgets()
        with self.canvas:
            for i in range(len(self.level["map_floor_0"])-1,-1,-1):
                for j in range(len(self.level["map_floor_0"][i])-1,-1,-1):
                    tile = self.level["map_floor_0"][i][j]
                    if tile!=0:
                        Rectangle(pos=[self.tile_offset[0]+(i-j)*self.tile_size[0]*0.5, self.tile_offset[1]+(i+j)*self.tile_size[1]*0.5], 
                                    size=self.tile_size, source=self.level["tiles"][str(tile)])

            for i in range(len(self.level["map_floor_0"])-1,-1,-1):
                for j in range(len(self.level["map_floor_0"][i])-1,-1,-1):
                    obj = self.level["map_floor_1"][i][j]
                    if obj!=0:
                        Rectangle(pos=[(self.tile_offset[0]+(i-j)*self.tile_size[0]*0.5)+self.tile_size[0]*0.5-self.object_size[0]*0.5, 
                                (self.tile_offset[1]+(i+j)*self.tile_size[1]*0.5)+self.tile_size[1]*0.5],
                                size=self.object_size, source=self.level["objects"][str(obj)])

        print(int(1/dt))


    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_move(self, touch):
        super().on_touch_move(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
