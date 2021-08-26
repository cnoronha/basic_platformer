import pygame
from random import randint

class Spikes(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/spikes.png').convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Sawman(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/saw_man.png').convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = move_x
        self.move_y = move_y
        self.move_direction = 2
        self.move_counter = 0
    
    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if self.move_counter > 20:
            self.move_direction *= -1
            self.move_counter *= -1

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit_door.png').convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/snow_platform.png').convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_x = move_x
        self.move_y = move_y
        self.move_direction = 1
        self.move_counter = 0
    
    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if self.move_counter > 20:
            self.move_direction *= -1
            self.move_counter *= -1


