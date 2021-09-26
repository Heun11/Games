import pygame as p
import pygame.freetype
from random import randint

p.init()

myfont = p.font.SysFont('Comic Sans MS', 60)
WIDTH = 500
HEIGHT = 800
screen = p.display.set_mode([WIDTH, HEIGHT])
p.display.set_caption("Flappy Bird")
clock = p.time.Clock()

# COLORS
BCK = (52, 235, 213)
BRD = (227, 25, 197)
PIP = (227, 181, 16)
TXT = (255, 0, 17)


# BIRD
class Bird:
    def __init__(self):
        self.x = 160
        self.y = HEIGHT/2
        self.r = 32

        self.gravity = 0.8
        self.vel = 0
        self.lift = -17

        self.dead = False

    def bounds(self):
        return p.Rect(self.x, self.y, self.r, self.r)

    def up(self):
        if self.dead != True:
            self.vel += self.lift

    def draw(self):
        p.draw.rect(screen, BRD, p.Rect(self.x, self.y, self.r, self.r))

        if self.dead:
            screen.blit(myfont.render(str("GAME OVER"), False, TXT),(100,200))
            screen.blit(myfont.render(str("Press Enter to restart"), False, TXT),(50,300))

    def update(self):
        self.vel += self.gravity
        self.vel *= 0.9

        self.y += self.vel

        if self.y > HEIGHT-8:
            self.y = HEIGHT-8
            self.vel = 0
        if self.y < 0:
            self.y = 0
            self.vel

# PIPES
class Pipe:
    def __init__(self,start):
        self.pos = [[start,400],[start,600]]
        self.w = 64
        self.h = 1000
        self.vel = 5

    def coll(self,r):
        if p.Rect(self.pos[0][0], 0, self.w, self.pos[0][1]).colliderect(r) or p.Rect(self.pos[1][0], self.pos[1][1], self.w, 50+HEIGHT-self.pos[1][1]).colliderect(r):
            return True

    def createPipes(self):
        x = randint(200, 600)

        self.pos = [[WIDTH+self.w,x-100],[WIDTH+self.w,x+100]]

    def draw(self):
        p.draw.rect(screen, PIP, p.Rect(self.pos[0][0], 0, self.w, self.pos[0][1]))
        p.draw.rect(screen, PIP, p.Rect(self.pos[1][0], self.pos[1][1], self.w, 50+HEIGHT-self.pos[1][1]))

        # p.draw.circle(screen, (255,0,0), (self.pos[0][0],self.pos[0][1]), 5) # horny
        # p.draw.circle(screen, (0,255,0), (self.pos[1][0],self.pos[1][1]), 5) # dolny
        

    def update(self):
        self.pos[0][0] -= self.vel
        self.pos[1][0] -= self.vel

        if self.pos[0][0] < 0-self.w:
            self.createPipes()




bird = Bird()
pipes = [Pipe(100),Pipe(350+64)]

# Main functions
def update():
    for pipe in pipes:
        pipe.update()
    bird.update()

    for pipe in pipes:
        if pipe.coll(bird.bounds()):
            bird.dead = True

def draw():
    screen.fill(BCK)

    for pipe in pipes:
        pipe.draw()
    bird.draw()

# main loop
run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    
        # KEYDOWN
        if event.type == p.KEYDOWN:
            if event.key == p.K_w:
                bird.up()

            if event.key == p.K_RETURN and bird.dead:
                print("ok")
                bird = Bird()
                pipes = [Pipe(100),Pipe(350+64)]
        
        # KEYUP
        if event.type == p.KEYUP:
            pass

    # main functions calling
    update()
    draw()

    # update display
    p.display.update()
    # fps
    clock.tick(60)

# quit
p.quit()

# FUCK