import pygame
import constants as const
import utility as util

# pylint: disable=no-member

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        image=pygame.image.load("")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))

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
        self