from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.graphics import Color

# FUNCTIONS

# Collision
def collide(rect1, rect2):
    r1 = {"x":rect1.pos[0], "y":rect1.pos[1], "w":rect1.size[0], "h":rect1.size[1]}
    
    # if x collide
    print("x")
    # if y collide
    print("y")

# CLASSES

# Entity class
class Entity:
    def __init__(self, size=(50,50), pos=(0,0), source=""):
        self.size = size
        self.pos = pos
        self.source = source
        self.rect = Rectangle(size=self.size,pos=self.pos,source=self.source)

    def get_bounds(self):
        return {"x":self.rect.pos[0],"y":self.rect.pos[1],"w":self.rect.size[0],"h":self.rect.size[1]}

    def draw(self):
        self.rect = Rectangle(size=self.size,pos=self.pos,source=self.source)

    def update(self):
        pass

# Player class
class Player(Entity):
    def __init__(self, size=(50,50), pos=(0,0), source=""):
        super().__init__(size, pos, source)
        self.vel = 3
        self.dir = {
            "up":False,
            "down":False,
            "right":False,
            "left":False
        }


    def draw(self):
        self.rect = Rectangle(size=self.size,pos=self.pos,source=self.source)

    def update(self):
        x_v = 0
        y_v = 0

        if self.dir["up"]:
            y_v = self.vel

        if self.dir["down"]:
            y_v = -self.vel

        if self.dir["right"]:
            x_v = self.vel

        if self.dir["left"]:
            x_v = -self.vel

        x = self.rect.pos[0]
        y = self.rect.pos[1]

        self.rect.pos = (x+x_v, y+y_v)

    def keys_down(self, key):
        # print(f"key {key} down")

        if key == "w" or key == "up":
            self.dir["up"] = True

        if key == "s" or key == "down":
            self.dir["down"] = True

        if key == "a" or key == "left":
            self.dir["left"] = True

        if key == "d" or key == "right":
            self.dir["right"] = True

    def keys_up(self, key):
        # print(f"key {key} up")

        if key == "w" or key == "up":
            self.dir["up"] = False

        if key == "s" or key == "down":
            self.dir["down"] = False

        if key == "a" or key == "left":
            self.dir["left"] = False

        if key == "d" or key == "right":
            self.dir["right"] = False

# Tile class
class Tile(Entity):
    def __init__(self, size, source=""):
        self.size = size
        self.source = source

    def draw(self, i, j):
        Rectangle(size=self.size, pos=(self.size[0]*i, self.size[1]*j), source=self.source)

# Object class
class Object(Tile):
    def __init__(self, size=(0,0), source=""):
        super().__init__(size=size, source=source)
