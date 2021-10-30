from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader

class Object:
    def __init__(self, size=(100,100), pos=(0,0), source=""):
        self.size = size
        self.pos = pos
        self.source = source

    def draw(self):
        Rectangle(size=self.size, pos=self.pos, source=self.source)

    def pressed(self, touch_pos):
        if ((touch_pos[0] > self.pos[0]) and (touch_pos[0] < self.pos[0]+self.size[0]) and
            (touch_pos[1] > self.pos[1]) and (touch_pos[1] < self.pos[1]+self.size[1])):
            self.on_press()

    def on_press(self):
        print(f"klikol si na {self}")

