import pygame as p
import random
import board

# vars
p.init()
screen_W = 600
screen_H = 600
screen = p.display.set_mode([screen_W, screen_H])
p.display.set_caption("TicTacToe")
clock = p.time.Clock()

b = board.Board()

# Main functions
def update():
    b.update()

def draw():
    screen.fill((250, 245, 232))

    b.draw(screen)


# main loop
run = True
while run:

    for event in p.event.get():
        # quit
        if event.type == p.QUIT:
            run = False

        # KEYDOWN
        if event.type == p.KEYDOWN:
            pass

        # KEYUP
        if event.type == p.KEYUP:
            pass

        b.getEvent(event)

    update()
    draw()

    # update display
    p.display.update()
    # fps
    clock.tick(60)

# quit
p.quit()
