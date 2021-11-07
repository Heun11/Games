from kivy.graphics import Rectangle

class GamePad:
    def __init__(self, screen_size, player):
        self.source="data/images/gamepad.png"
        self.size=screen_size[0]*0.3
        self.pos=[screen_size[0]*0.35, screen_size[1]*0.2]
        self.player=player

    def update(self):
        Rectangle(source=self.source, pos=self.pos, size=[self.size, self.size])

    def on_touch(self, touch):
        pos=touch.pos
        size_of_btn=self.size/3

        # collision
        # if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+self.size[0]) and
        #     (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+self.size[1])):

        if ((pos[0] > self.pos[0]+size_of_btn) and (pos[0] < self.pos[0]+size_of_btn*2) and
            (pos[1] > self.pos[1]+size_of_btn*2) and (pos[1] < self.pos[1]+self.size)):
            print("up")
            self.player.move(0)

        if ((pos[0] > self.pos[0]+size_of_btn) and (pos[0] < self.pos[0]+size_of_btn*2) and
            (pos[1] > self.pos[1]) and (pos[1] < self.pos[1]+size_of_btn)):
            print("down")
            self.player.move(1)

        if ((pos[0] > self.pos[0]+size_of_btn*2) and (pos[0] < self.pos[0]+self.size) and
            (pos[1] > self.pos[1]+size_of_btn) and (pos[1] < self.pos[1]+size_of_btn*2)):
            print("right")
            self.player.move(2)

        if ((pos[0] > self.pos[0]) and (pos[0] < self.pos[0]+size_of_btn) and
            (pos[1] > self.pos[1]+size_of_btn) and (pos[1] < self.pos[1]+size_of_btn*2)):
            print("left")
            self.player.move(3)

class Player:
    def __init__(self, screen_size):
        self.source=""
        self.size=screen_size[0]*0.1
        self.pos=[screen_size[0]*0.3, screen_size[1]*0.4]
        self.screen_size=screen_size
        self.dirs=[self.size, -self.size, self.size, -self.size]

    def update(self):
        Rectangle(pos=self.pos, size=[self.size, self.size], source=self.source)

    def move(self, d):
        if d<=1:
            self.pos[1]+=self.dirs[d]
        else:
            self.pos[0]+=self.dirs[d]
