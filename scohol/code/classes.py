from kivy.graphics import Rectangle, Color
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

        self.end=False

    def update(self):
        Rectangle(pos=[0,0], size=self.sc, source="data/images/road.png")

        if self.player.dead:
            self.end=True

        self.score_counter.update()
        self.enemy_loader.update()
        self.player.collide(self.enemy_loader.get_enemies())
        self.player.update()

    def on_touch_down(self, touch):
        if touch.pos[0]<self.sc[0]/2:
            self.player.move(-1)
        else:
            self.player.move(+1)

    def on_touch_up(self, touch):
        pass

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
        self.source="data/images/player1.png"
        self.size=sc[0]*0.25
        self.pos=[sc[0]*0.25,sc[1]*0.25]
        self.dead=False

    def update(self):
        Rectangle(pos=self.pos, size=[self.size, self.size], source=self.source)

    def collide(self, enemies):
        for enemy in enemies:
            if(self.pos[0]<enemy.pos[0]+enemy.size[0] and
            self.pos[0]+self.size>enemy.pos[0] and
            self.pos[1]<enemy.pos[1]+enemy.size[1] and
            self.size+self.pos[1]>enemy.pos[1]):
                self.dead=True

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
        self.enemies={
            0:[],
            1:[],
            2:[],
            3:[]
        }
        self.empty_road=random.randint(0, 3)

    def update(self):
        for road in range(4):
            for enemy in self.enemies[road]:
                enemy.update()
                if enemy.dead:
                    self.enemies[road].remove(enemy)
                    self.empty_road=road
        self.spawn()

    def spawn(self):
        for road in range(4):
            if road != self.empty_road:
                if len(self.enemies[road])<1:
                    type_of_new_enemy=random.randint(1,2)
                    if type_of_new_enemy==1:
                        self.enemies[road].append(Bus(sc=self.sc, road=road))
                    elif type_of_new_enemy==2:
                        self.enemies[road].append(Car(sc=self.sc, road=road))
                    elif type_of_new_enemy==3:
                        self.enemies[road].append(Pillar(sc=self.sc, road=road))
    
    def get_enemies(self):
        l = []
        for road in range(4):
            for enemy in self.enemies[road]:
                l.append(enemy)
        return l

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

class Bus(Enemy):
    def __init__(self, sc, road=0):
        super().__init__(sc, road=road)
        self.size[1]=sc[1]*random.uniform(0.2, 0.4)
        self.sources=["data/images/bus1.png","data/images/bus1.png","data/images/bus1.png"]
        self.source=self.sources[random.randint(0,2)]
        self.type="bus"

class Car(Enemy):
    def __init__(self, sc, road=0):
        super().__init__(sc, road=road)
        self.size[1]=sc[1]*random.uniform(0.15, 0.25)
        self.sources=["data/images/car1.png","data/images/car1.png","data/images/car1.png"]
        self.source=self.sources[random.randint(0,2)]
        self.type="car"

class Pillar(Enemy):
    def __init__(self, sc, road=0):
        super().__init__(sc, road=road)
        self.size[1]=sc[0]*0.25
        self.speed=sc[1]//192
        self.source="data/images/pillar.png"
        self.type="pillar"
