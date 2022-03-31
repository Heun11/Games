import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(block_size*2,block_size*2,block_size*0.75,block_size)
        self.xVel = 0
        self.yVel = 0

        self.speed = block_size/15
        self.gravity = block_size/90
        self.jump_speed = -(block_size/3.75)
        self.on_ground = False

    def collision_horizontal(self, blocks):
	#	    if tile.colliderect(self.rect):
	#    	        if self.xVel>0:
	#		    self.rect.x = tile.x-self.rect.width
	#		elif self.xVel<0:
	#	            self.rect.x = tile.x+tile.width
        for block in blocks:
            if block.colliderect(self.rect):
                if self.xVel>0:
                    self.rect.x = block.x-self.rect.width
                elif self.xVel<0:
                    self.rect.x = block.x+block.width


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

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.xVel = -1
        elif keys[pygame.K_d]:
            self.xVel = 1
        else:
            self.xVel = 0
		
        if keys[pygame.K_SPACE]:
            self.jump()

    def update(self, screen, blocks):
        self.get_input()

	#self.yVel += self.gravity
        #self.rect.y += self.yVel
	#self.collision_vertical(blocks)

        self.rect.x += self.xVel * self.speed
        self.collision_horizontal(blocks)

        pygame.draw.rect(screen, (0,0,255), self.rect)


