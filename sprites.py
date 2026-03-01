import pygame
import constants as const
import utility as util

# pylint: disable=no-member

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        image=pygame.image.load("assets/sprite_standing.png")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()
        self.rect= x
        self.rect = y


    def move(self):
        if self.x == pygame.K_LEFT:
            self.x +=10
        elif self.x == pygame.K_RIGHT:
            self.x -=10
        if self.y == pygame.K_UP:
            self.y +=10
        elif self.y == pygame.K_DOWN:
            self.y -=10

        

    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        
class Hinder(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        image=pygame.image.load("")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()
        self.rect= x
        self.rect = y

    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))