# Pygame template - skeleton for a new pygame project
import pygame
import random
import os
import math

WIDTH = 1024
HEIGHT = 768
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
asset_folder = os.path.join(game_folder, 'assets')

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player_img_full= pygame.image.load(os.path.join(asset_folder, 'redcar.png')).convert()
player_img = pygame.transform.scale(player_img_full, (64, 32))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.direction = 0
        self.speed = 5

    def update(self):
        self.rect.x += math.sin(self.direction)*self.speed
        self.rect.y += math.cos(self.direction)*self.speed
        self.image = pygame.transform.rotozoom(player_img, math.degrees(self.direction)-90, 1)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.rect.left > WIDTH:
            self.rect.right = 0

player = Player()
all_sprites.add(player)

# Game loop
running = True
player_dirchange = 0
while running:
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dirchange = 0.1
            if event.key == pygame.K_RIGHT:
                player_dirchange = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_dirchange = 0

    player.direction += player_dirchange

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(GREEN)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()
	
	# keep loop running at the right speed
    clock.tick(FPS)

pygame.quit()