from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader
import random, json    

def load_high_score():
    with open("data/save.json") as f:
        return json.load(f)["h_score"]

def save_high_score(score):
    x=False
    with open("data/save.json", "r") as f:
        data=json.load(f)
        if score > data["h_score"]:
            data["h_score"]=score
            x=True
    if x:
        with open("data/save.json", "w") as f:
            json.dump(data, f, indent=2)

class Game:
    def __init__(self, sc):
        self.sc=sc
        self.player=Player(sc=sc)
        self.enemy_loader=EnemyLoader(sc=sc)
        self.score_counter=ScoreCounter()

        self.background_music=SoundLoader.load("data/sounds/background_music.wav")
        self.background_music.loop=True
        self.background_music.play()

        self.end=False

    def update(self):
        Rectangle(pos=[0,0], size=self.sc, source="data/images/debili/road.png")

        if self.player.dead:
            self.end=True
            self.background_music.stop()
        else:
            self.score_counter.update()
            self.enemy_loader.update()
            self.player.collide(self.enemy_loader.get_enemies())
            self.player.update()

    def on_touch_down(self, touch):
        if touch.pos[0]<self.sc[0]/2:
            self.player.move(-1)
        else:
            self.player.move(+1)

class ScoreCounter:
    def __init__(self):
        self.score=0
        self.x=0
    
    def update(self):
        self.x+=1
        if self.x%10==0:
            self.score+=1

    def get_score(self):
        return self.score

class Player:
    def __init__(self, sc):
        self.sc=sc
        self.source="data/images/debili/player1.png"
        self.size=sc[0]*0.25
        self.pos=[sc[0]*0.25,sc[1]*0.25]
        self.dead=False
        self.ouch=SoundLoader.load("data/sounds/ouch.wav")

    def update(self):
        Rectangle(pos=self.pos, size=[self.size, self.size], source=self.source)

    def collide(self, enemies):
        for enemy in enemies:
            if(self.pos[0]<enemy.pos[0]+enemy.size[0] and
            self.pos[0]+self.size>enemy.pos[0] and
            self.pos[1]<enemy.pos[1]+enemy.size[1] and
            self.size+self.pos[1]>enemy.pos[1]):
                self.dead=True
                self.ouch.play()

    def move(self, dir_):
        if dir_>0:
            if self.pos[0]<self.sc[0]-self.size:
                self.pos[0]+=self.size
        else:
            if self.pos[0]>0:
                self.pos[0]-=self.size

class EnemyLoader:
    def __init__(self, sc):
        self.sc=sc
        self.size=sc[0]*0.25

        self.enemies = [Empty(sc=self.sc),Empty(sc=self.sc),Empty(sc=self.sc),Empty(sc=self.sc)]
        self.empty_road=random.randint(0, 3)

    def update(self):
        for road, enemy in enumerate(self.enemies):
            enemy.update()
            if enemy.dead:
                self.enemies[road]=Empty(sc=self.sc)
                self.empty_road=road
        self.spawn()

    def spawn(self):
        for road, enemy in enumerate(self.enemies):
            if road != self.empty_road:
                if isinstance(enemy, Empty):
                    type_of_new_enemy=random.randint(1,2)
                    if type_of_new_enemy==1:
                        self.enemies[road]=Bus(sc=self.sc, road=road)
                    elif type_of_new_enemy==2:
                        self.enemies[road]=Car(sc=self.sc, road=road)
    
    def get_enemies(self):
        return self.enemies

class Enemy:
    def __init__(self, sc, road=0):
        self.sc=sc
        self.source=""
        self.road=road
        self.size=[sc[0]*0.25, sc[1]*0.2]
        self.pos=[self.size[0]*self.road,sc[1]]
        self.speed=random.randint(sc[1]//120, sc[1]//64)
        self.dead=False
        self.type="enemy"

    def update(self):
        Rectangle(pos=self.pos, size=self.size, source=self.source)
        self.pos[1]-=self.speed
        if self.pos[1]<0-self.size[1]:
            self.dead=True

class Empty(Enemy):
    def __init__(self, sc, road=0):
        super().__init__(sc, road=road)

    def update(self):
        pass

class Bus(Enemy):
    def __init__(self, sc, road=0):
        super().__init__(sc, road=road)
        self.size[1]=sc[1]*random.uniform(0.2, 0.4)
        self.sources=["data/images/debili/bus1.png","data/images/debili/bus2.png"]
        self.source=self.sources[random.randint(0,1)]
        self.type="bus"

class Car(Enemy):
    def __init__(self, sc, road=0):
        super().__init__(sc, road=road)
        self.size[1]=sc[1]*random.uniform(0.15, 0.25)
        self.sources=["data/images/debili/car1.png","data/images/debili/car2.png","data/images/debili/car3.png"]
        self.source=self.sources[random.randint(0,2)]
        self.type="car"
