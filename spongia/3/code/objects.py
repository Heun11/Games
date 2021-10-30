from kivy.graphics import Rectangle
from kivy.graphics import Color

class Object:
    def __init__(self, size=[50,50], pos=[0,0], source=""):
        self.pos = pos
        self.size = size
        self.source = source

    def update_draw(self):
        Rectangle(source=self.source, pos=self.pos, size=self.size)