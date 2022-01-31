from kivy.graphics import Rectangle
import random, json

from .sounds import Sound

class Background:
    def __init__(self, size=(100,100), pos=(0,0), source=""):
        self.size = size
        self.pos = pos
        self.source = source

    def update(self):
        Rectangle(size=self.size, pos=self.pos, source=self.source)

class Player:
    def __init__(self, size=(0.1,0.1), pos=(0,0), ms=[[0,0],[0,0]], screen_size=(0,0)):
        self.size = [screen_size[0]*size[0], screen_size[1]*size[1]]
        self.pos = [screen_size[0]*pos[0], screen_size[1]*pos[1]]
        self.movable_space = ms
        self.images = {
            "stand":[""],
            "walking":["", ""]
        }
        self.walking = {"is":False, "dest":[0,0], "speed":screen_size[0]/366}
        self.inventory = []

    def update(self):
        if self.walking["is"]:
            if self.pos == self.walking["dest"]:
                self.walking["is"]=False
            else:
                if self.pos[0]>self.walking["dest"][0]:
                    self.pos = (self.pos[0]-self.walking["speed"], self.pos[1])
                if self.pos[0]<self.walking["dest"][0]:
                    self.pos = (self.pos[0]+self.walking["speed"], self.pos[1])
                if self.pos[1]>self.walking["dest"][1]:
                    self.pos = (self.pos[0], self.pos[1]-self.walking["speed"])
                if self.pos[1]<self.walking["dest"][1]:
                    self.pos = (self.pos[0], self.pos[1]+self.walking["speed"]) 
        # else:
        #     Rectangle(size=self.size, pos=self.pos, source=self.images["stand"][0])
        Rectangle(size=self.size, pos=self.pos, source=self.images["stand"][0])

    def touch_down(self, pos):
        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+self.size[0]) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+self.size[1])):
            self.on_press()
        else:
            self.move(pos)

    def on_press(self):
        print("ouch!")

    def move(self, pos):
        if ((pos[0]>=self.movable_space[0][0] and pos[0]<=self.movable_space[0][1]) and
            (pos[1]>=self.movable_space[1][0] and pos[1]<=self.movable_space[1][1])):
            self.walking["is"], self.walking["dest"] = True, pos

# OBJECT <
class Object:
    def __init__(self, size=(0.1,0.1), pos=(0,0), source="", screen_size=(0,0)):
        self.size = [screen_size[0]*size[0], screen_size[1]*size[1]]
        self.pos = [screen_size[0]*pos[0], screen_size[1]*pos[1]]
        self.source = source

    def update(self):
        Rectangle(size=self.size, pos=self.pos, source=self.source)

    def touch_down(self, pos):
        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+self.size[0]) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+self.size[1])):
            self.on_press()

    def on_press(self):
        print(f"klikol si na {self}")

class Door(Object):
    def __init__(self, size=(0.1,0.1), pos=(0, 0), source="", scene=0, screen_size=[0,0]):
        super().__init__(size=size, pos=pos, source=source, screen_size=screen_size)
        self.scene = scene
        self.sound = Sound(path="data/sounds/knock_knock.wav", loop=False, volume=0.6)

    def on_press(self):
        print("knock knock!")
        self.sound.play()
        # with open("data/save.json", "w") as f:
        #     json.dump({"ac_scene":self.scene}, f, indent=2)

class Picture(Object):
    def __init__(self, size=(0.1,0.1), pos=(0,0), source="", screen_size=(0,0)):
        super().__init__(size=size, pos=pos, source=source, screen_size=screen_size)
        self.sound = Sound(path="data/sounds/blue_slide_park.wav", loop=False, volume=0.1)

    def on_press(self):
        print("It's f*cking blue slide park man..., It's f*cking blue slide park...")
        self.sound.play()

class Computer(Object):
    def __init__(self, size=(0.1,0.1), pos=(0,0), screen_size=(0,0)):
        self.source = f"data/images/pc{random.randint(0,2)}.png"
        super().__init__(size=size, pos=pos, source=self.source, screen_size=screen_size)

    def on_press(self):
        self.source = f"data/images/pc{random.randint(0,2)}.png"

class Switch(Object):
    def __init__(self, size=(0.1, 0.1), pos=(0, 0), source="", screen_size=(0, 0)):
        super().__init__(size=size, pos=pos, source=source, screen_size=screen_size)
        self.state = False

    def on_press(self):
        print("debil")
# OBJECT >