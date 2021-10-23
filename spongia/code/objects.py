from kivy.graphics import Rectangle

class StaticObject:
    def __init__(self, size=[50,50], pos=[0,0], source=""):
        self.pos = pos
        self.size = size
        self.source = source

    def draw(self):
        Rectangle(source=self.source, pos=self.pos, size=self.size)