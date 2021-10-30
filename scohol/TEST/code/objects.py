from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader

class Object:
    def __init__(self, size=(100,100), pos=(0,0), source=""):
        self.size = size
        self.pos = pos
        self.source = source

    def update(self):
        Rectangle(size=self.size, pos=self.pos, source=self.source)

    def touch_down(self, pos):
        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+self.size[0]) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+self.size[1])):
            self.on_press()

    def on_press(self):
        print(f"klikol si na {self}")