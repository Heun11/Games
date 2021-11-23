from kivy.graphics import Rectangle, Color

class Entity:
    def __init__(self, sc, pos=[0,0], size=[0.1,0.1], images=[""]):
        self.pos=[sc[0]*pos[0], sc[1]*pos[1]]
        self.size=[sc[0]*size[0], sc[0]*size[1]]
        self.images=images

    def update(self):
        if len(self.images)<=1:
            s=self.images[0]
        else:
            # Animation update
            s=self.images[0]

        Rectangle(pos=self.pos, size=self.size, source=s)

def load_level(index):
    if index == 0:
        return {"player":{"pos":[0.1,0.1]}} # TAKTO NEJAKO

    else:
        return "NO LEVEL FOUND"