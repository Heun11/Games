from kivy.graphics import Rectangle

class Player:
    def __init__(self, screen_size):
        # self.source="data/images/player.png"
        self.source=""
        self.size=screen_size[0]*0.1
        self.pos=[screen_size[0]*0.45, screen_size[1]*0.3]
        self.screen_size=screen_size

        self.vel = 0
        self.gravity = -150

        self.dir = None
        self.speed=5

    def t_down(self, pos):
        if pos[0]>self.screen_size[0]*0.5:
            self.dir="r"
        else:
            self.dir="l"

    def t_up(self):
        self.dir=None

    def update(self, dt, platforms):
        for p in platforms:
            platform = p.get_bounds()

            if (((self.pos[0]>platform["x"] and self.pos[0]<platform["x"]+platform["w"]) or 
            (self.pos[0]+self.size<platform["x"]+platform["w"] and self.pos[0]+self.size>platform["x"])) and
            (self.pos[1]>platform["y"] and self.pos[1]<platform["y"]+platform["h"])):
                self.vel=300

        self.pos = [self.pos[0], self.pos[1]+dt*self.vel]
        self.vel +=dt*self.gravity

        if self.dir=="l":
            self.pos[0]-= self.speed
        if self.dir=="r":
            self.pos[0]+=self.speed

        if self.pos[0]>self.screen_size[0]-self.size:
            self.pos[0]=0
        if self.pos[0]<0:
            self.pos[0]=self.screen_size[0]-self.size

        Rectangle(pos=self.pos, size=[self.size, self.size], source=self.source)

class Platform:
    def __init__(self, screen_size, pos):
        self.source=""
        self.pos=[screen_size[0]*pos[0], screen_size[1]*pos[1]]
        self.size=[screen_size[0]*0.15, screen_size[0]*0.1*.25]
        self.screen_size=screen_size
    
    def get_bounds(self):
        return {"x":self.pos[0], "y":self.pos[1], "w":self.size[0], "h":self.size[1]}

    def update(self):
        Rectangle(pos=self.pos, size=self.size, source=self.source)