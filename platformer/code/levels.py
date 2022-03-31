import pygame
from . import WIDTH, HEIGHT, screen

class Block():
    def __init__(self, i, j, block_size):
        self.rect = pygame.Rect(j*block_size,i*block_size, block_size-1,block_size-1)

def update_level(INDEX, player):
    if INDEX==0:
        blocks = []
        level_width = 20
        level_height = 20 
        
        if level_width>level_height:
            block_size = WIDTH/level_width
        else:
            block_size = HEIGHT/level_height

        for i in range(10):
            blocks.append(Block(10,i,block_size))

        for b in blocks:
            pygame.draw.rect(screen, (0,255,0), b.rect)

        player.update(screen, blocks, block_size)

