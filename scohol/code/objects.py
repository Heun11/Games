from kivy.graphics import Rectangle

class GamePad:
    def __init__(self, screen_size=[0,0], size=[0.1,0.1], pos=[0.1,0.1], player=None):
        self.source=""
        self.size=[screen_size[0]*size[0], screen_size[1]*size[1]]
        self.pos=[screen_size[0]*pos[0], screen_size[1]*pos[1]]
        self.screen_size=screen_size
        self.player=player

    def update(self):
        Rectangle(source=self.source, pos=self.pos, size=self.size)

    def on_touch(self, touch):
        pos=touch.pos
        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+self.size[0]) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+self.size[1])):
            print("debil")

class Player:
    def __init__(self, screen_size=[0,0], size=[0.1,0.1], pos=[0.1,0.1]):
        self.source=""
        self.size=[screen_size[0]*size[0], screen_size[1]*size[1]]
        self.pos=[screen_size[0]*pos[0], screen_size[1]*pos[1]]
        self.screen_size=screen_size

    def update(self):
        Rectangle(pos=self.pos, size=self.size, source=self.source)

    def move(self):
        pass