import pygame
pygame.init()

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Platformer Demo')
clock = pygame.time.Clock()

level = [
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
block_size = 45

class Player:
	def __init__(self):
		self.image = pygame.image.load("data/images/player.png")
		self.image = pygame.transform.scale(self.image, [block_size, block_size])
		self.rect = pygame.Rect(block_size*2,block_size*2,block_size,block_size)
		self.xVel = 0
		self.yVel = 0

		self.speed = 3
		self.gravity = 0.5
		self.jump_speed = -12
		self.on_ground = False

		self.aim_dir = "n" #n-None l-left, r-right, u-up, d-down
		self.can_shoot = True # set this to be true again, if the arrow will stop

	def collision_horizontal(self, level):
		self.rect.x += player.xVel * self.speed

		for i in range(len(level)):
			for j in range(len(level[i])):
				if level[i][j]==1:
					tile = pygame.Rect(j*block_size,i*block_size, block_size,block_size)
					if tile.colliderect(self.rect):
						if self.xVel>0:
							self.rect.x = tile.x-self.rect.width
						elif self.xVel<0:
							self.rect.x = tile.x+tile.width

		self.rect.x -= player.xVel * self.speed

	def collision_vertical(self, level):
		for i in range(len(level)):
			for j in range(len(level[i])):
				if level[i][j]==1:
					tile = pygame.Rect(j*block_size,i*block_size, block_size,block_size)
					if tile.colliderect(self.rect):
						if self.yVel>0:
							self.rect.y = tile.y-self.rect.height
							self.yVel = 0
							self.on_ground = True
						elif self.yVel<0:
							self.rect.y = tile.y+tile.height
							self.yVel = 0

	def jump(self):
		if self.on_ground:
			self.yVel = self.jump_speed
			self.on_ground = False

	def shoot(self):
		if self.aim_dir!="n" and self.can_shoot:
			self.can_shoot = False
			if self.aim_dir == "u":
				print("shooting up")
			elif self.aim_dir == "d":
				print("shooting down")
			elif self.aim_dir == "l":
				print("shooting left")
			elif self.aim_dir == "r":
				print("shooting right")

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.xVel = -1
		elif keys[pygame.K_d]:
			self.xVel = 1
		else:
			self.xVel = 0
		
		if keys[pygame.K_w]:
			self.jump()

		if keys[pygame.K_UP]:
			self.aim_dir = "u"
		elif keys[pygame.K_DOWN]:
			self.aim_dir = "d"
		elif keys[pygame.K_LEFT]:
			self.aim_dir = "l"
		elif keys[pygame.K_RIGHT]:
			self.aim_dir = "r"
		else:
			self.aim_dir = "n"

		if keys[pygame.K_SPACE]:
			self.shoot()

	def update(self):
		self.get_input()

		self.yVel += self.gravity
		self.rect.y += self.yVel
		self.collision_vertical(level)

		self.rect.x += self.xVel * self.speed
		self.collision_horizontal(level)

		# print(self.rect.x, self.rect.y, self.xVel, self.yVel)
		# print(self.aim_dir)

		# pygame.draw.rect(screen, (0,0,255), self.rect)
		screen.blit(self.image, [self.rect.x, self.rect.y])


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


	update()
	clock.tick(60)
	# print(clock.get_fps())
