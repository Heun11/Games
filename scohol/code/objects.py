from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader
from .classes import Object

SOUNDS = {
    "music_box":SoundLoader.load("data/sounds/music_box.mp3")
}

def play_music(name):
    for i in SOUNDS:
        SOUNDS[i].stop()
    SOUNDS[name].play()

class MusicBox(Object):
    def __init__(self, size=(100, 100), pos=(0, 0), source=""):
        super().__init__(size=size, pos=pos, source=source)
    
    def on_press(self):
        super().on_press()
        play_music("music_box")

class MoveBox(Object):
    def __init__(self, size=(100, 100), pos=(0, 0), source=""):
        super().__init__(size=size, pos=pos, source=source)
    
    def on_press(self):
        super().on_press()
        self.pos = [self.pos[0]+20, self.pos[1]+10]

class Player:
    def __init__(self, size=(100,100), pos=(0,0), source="", movable_space={"x":[100,100], "y":[100,100]}):
        self.size = size
        self.pos = pos
        self.source = source
        self.movable_space = movable_space

    def draw(self):
        Rectangle(size=self.size, pos=self.pos, source=self.source)

    def pressed(self, touch_pos):
        if ((touch_pos[0] > self.pos[0]) and (touch_pos[0] < self.pos[0]+self.size[0]) and
            (touch_pos[1] > self.pos[1]) and (touch_pos[1] < self.pos[1]+self.size[1])):
            self.wiggle()
        else:
            if ((touch_pos[0] > self.movable_space["x"][0]) and (touch_pos[0] < self.movable_space["x"][1]) and
            (touch_pos[1] > self.movable_space["y"][0]) and (touch_pos[1] < self.movable_space["y"][1])):
                self.move(touch_pos)

    def wiggle(self):
        # play wiggle animation
        print("wiggle")

    def move(self, pos):
        pass
            