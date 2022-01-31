import pygame
pygame.init()

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Platformer Demo')
clock = pygame.time.Clock()

level = [
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
block_size = 45

class Player:
	def __init__(self):
		self.rect = pygame.Rect(block_size,block_size,block_size,block_size)
		self.xVel = 0
		self.yVel = 0

	def jump(self):
		print("jump")

	def update(self):
		self.rect.y+=self.yVel
		self.rect.x+=self.xVel
		pygame.draw.rect(screen, (0,0,255), self.rect)

player = Player()

def update():
	screen.fill((20,20,20))

	for i in range(len(level)):
		for j in range(len(level[i])):
			if level[i][j]==1:
				pygame.draw.rect(screen, (0,255,0), pygame.Rect(j*block_size,i*block_size, block_size-1,block_size-1))

	player.update()

	pygame.display.update()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

			if event.key == pygame.K_SPACE:
				player.jump()


	update()
	clock.tick(120)
