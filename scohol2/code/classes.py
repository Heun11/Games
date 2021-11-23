from kivy.graphics import Rectangle, Color
import random

class Game:
    def __init__(self, sc):
        self.sc=sc
        self.speed=1
        
        self.enemy_loader=EnemyLoader(sc=sc)
        self.player=Player(sc=sc)

    def update(self, dt):
        Rectangle(pos=[0,0], size=[self.sc[0], self.sc[1]*0.4], source="data/images/road.png")

        self.enemy_loader.update()
        self.player.update()

        Rectangle(pos=[0,0], size=[self.sc[0], self.sc[1]*0.15], source="data/images/bar.png")

    def on_touch_down(self, touch):
        self.player.move(touch.pos)
    
    def on_touch_up(self, touch):
        pass

class EnemyLoader:
    def __init__(self, sc):
        self.sc=sc
        self.size=sc[0]*0.25

        self.enemies=[Empty(),Empty(),Empty(),Empty()]
        # self.enemies=[Enemy(sc=sc, road=1), Enemy(sc=sc, road=2)]
        self.empty_road=random.randint(0, 3)

    def update(self):
        for road, enemy in enumerate(self.enemies):
            enemy.update()

            if enemy.dead:
                self.enemies[road]=Empty()
                self.empty_road=road

        self.spawn()
        
    def spawn(self):
        for road, enemy in enumerate(self.enemies):
            if road != self.empty_road:
                if isinstance(enemy, Empty):
                    self.enemies[road]=Enemy(sc=self.sc, road=road)

class Enemy:
    def __init__(self, sc, road=0):
        self.sc=sc
        self.source="data/images/bus.png"

        self.road=road

        self.target_size=[sc[0]*0.25, sc[1]*0.25]

        self.size=[sc[0]*0.1,sc[1]*0.1]
        self.pos=[self.road*(sc[0]*0.25),sc[1]*0.4]

        self.speed=random.uniform(0.5,1)
        self.brightness=0.1

        self.dead=False
        self.fs=False

    def update(self):
        if self.pos[1]<0:
            self.dead=True

        self.pos[1]-=self.speed*2.5

        if self.brightness<1:
            self.brightness+=self.speed*0.05

        if self.size[0]<self.target_size[0]:
            self.size[0]+=self.speed
            self.size[1]+=self.speed
        else:
            self.fs=True

        self.pos[0]=self.road*(self.sc[0]*0.25)+self.target_size[0]*0.5-self.size[0]*0.5

        Color(1,1,1,self.brightness)
        Rectangle(pos=self.pos, size=self.size, source=self.source)
        Color(1,1,1,1)

class Empty(Enemy):
    def __init__(self):
        super().__init__([0,0])

    def update(self):
        pass

class Player:
    def __init__(self, sc):
        self.sc=sc

        self.road=0
        self.source="data/images/player.png"

        self.size=sc[0]*0.25
        self.pos=[self.road*self.size, sc[1]*0.2]

        self.dead=False

    def update(self):
        Rectangle(pos=self.pos, size=[self.size, self.size], source=self.source)
        self.pos[0]=self.road*self.size

        if self.dead:
            print("dead")

    def collide(self, enemies):
        for enemy in enemies:
            if enemy.fs and enemy.pos[1]<self.pos[1]+self.size:
                self.dead=True

    def move(self, pos):
        if pos[0]>self.sc[0]*0.5 and self.road<3:
            self.road+=1
        elif pos[0]<self.sc[0]*0.5 and self.road>0:
            self.road-=1
