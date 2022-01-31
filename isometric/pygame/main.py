import pygame
pygame.init()

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Isometric Demo')

textures = {}
for i in range(5):
	textures[i] = pygame.image.load(f"data/{i}.png")

tile_size = [96, 48]
tile_offset = [350,120]

map_ = [
	[1,1,1,1,1,1,1,1,1,1],
	[1,2,2,2,2,2,2,2,2,1],
	[1,2,4,4,4,4,4,0,2,1],
	[1,2,0,0,0,0,0,0,2,1],
	[1,2,0,0,3,3,3,0,2,1],
	[1,2,0,0,0,3,3,3,2,1],
	[1,2,2,2,2,2,2,2,2,1],
	[1,1,1,1,1,1,1,1,1,1]
]

def update():
	screen.fill((20,20,20))

	for y in range(len(map_)):
		for x in range(len(map_[0])):
			screen.blit(textures[map_[y][x]], ((x-y)*(tile_size[0]/2)+tile_offset[0], 
												(x+y)*(tile_size[1]/2)+tile_offset[1]))

	pygame.display.update()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	update()
