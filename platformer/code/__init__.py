import pygame
pygame.init()

WIDTH = 1024
HEIGHT = 712
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Platformer Demo')
clock = pygame.time.Clock()

from .levels import update_level
from .player import Player

player = Player()

def update():
        screen.fill((255,255,255))
        update_level(0, player)
        pygame.display.update()

def run():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		update()
		clock.tick(60)
		# print(clock.get_fps())
