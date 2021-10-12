import lib
import pygame as p
from random import randint

p.init()

WIDTH = 400
HEIGHT = 400
screen = p.display.set_mode([WIDTH, HEIGHT])
p.display.set_caption("AnimTest")
clock = p.time.Clock()

# COLORS
BCK = (0, 0, 0)

img_folder = "TEST_DATA/"
# IMAGES = [img_folder+"1.png",img_folder+"2.png",img_folder+"3.png", img_folder+"2.png", img_folder+"1.png"]
# IMAGES = [img_folder+"attack_1.png", img_folder+"attack_2.png", img_folder+"attack_3.png", img_folder+"attack_4.png", img_folder+"attack_5.png", 
#             img_folder+"attack_6.png", img_folder+"attack_7.png", img_folder+"attack_8.png", img_folder+"attack_9.png", img_folder+"attack_10.png"]

RUN = [img_folder+"run/1.png",img_folder+"run/2.png",img_folder+"run/3.png",img_folder+"run/4.png",
        img_folder+"run/5.png",img_folder+"run/6.png",img_folder+"run/7.png",img_folder+"run/8.png"]
ROLL = [img_folder+"roll/1.png",img_folder+"roll/2.png",img_folder+"roll/3.png",img_folder+"roll/4.png",img_folder+"roll/5.png",
        img_folder+"roll/6.png",img_folder+"roll/7.png",img_folder+"roll/8.png", img_folder+"roll/9.png", img_folder+"roll/10.png"]
STAND = img_folder+"original/1.png"
COMBAT = [img_folder+"combat/1.png",img_folder+"combat/2.png",img_folder+"combat/3.png",img_folder+"combat/4.png",img_folder+"combat/5.png",
        img_folder+"combat/6.png",img_folder+"combat/7.png",img_folder+"combat/8.png", img_folder+"combat/9.png", img_folder+"combat/10.png"]

class Test:
    def __init__(self):
        self.current_animation = "stand"
        self.animations = {
            "run":lib.animation.Animation(speed=13, frames=RUN),
            "roll":lib.animation.Animation(speed=10, frames=ROLL),
            "stand":lib.animation.Animation(speed=10, frames=[STAND]),
            "combat":lib.animation.Animation(speed=13, frames=COMBAT)
        }

    def draw(self):
        screen.blit(p.transform.scale(p.image.load(self.animations[self.current_animation].get_current_frame()), (300,300)), (0, 50))

    def update(self):
        for i in self.animations:
            if i == self.current_animation:
                self.animations[i].update()
            else:
                self.animations[i].restart()


player = Test()

# Main functions
def update():
    player.update()

def draw():
    screen.fill(BCK)
    player.draw()

# main loop
run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        # KEYDOWN
        if event.type == p.KEYDOWN:
            if event.key == p.K_d:
                player.current_animation = "run"

            if event.key == p.K_s:
                player.current_animation = "roll"

            if event.key == p.K_w:
                player.current_animation = "combat"

        # KEYUP
        if event.type == p.KEYUP:
            player.current_animation = "stand"

    # main functions calling
    update()
    draw()

    # update display
    p.display.update()
    # fps
    clock.tick(60)

# quit
p.quit()
