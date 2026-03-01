import pygame
import constants as const
import utility as util

# pylint: disable=no-member

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        image=pygame.image.load("assets/playerUp1.png")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()
        self.rect= x
        self.rect = y
        self.speed=10
        self.moving=False


        self.direction=1
        self.whichImage=1
        self.counter=0
        self.imageRight=[pygame.transform.scale(pygame.image.load("assets/playerUp1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight1.png"),(width, height))]#[pygame.transform.scale(pygame.image.load("assets/playerRight1"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]
        self.imageLeft=[pygame.transform.scale(pygame.image.load("assets/playerUp1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight1.png"),(width, height))]#[pygame.transform.scale(pygame.image.load("assets/playerLeft1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]
        self.imageUp=[pygame.transform.scale(pygame.image.load("assets/playerUp1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight1.png"),(width, height))]
        self.images=self.imageUp

    def move(self, event):
        if event.key == pygame.K_LEFT:
            self.moving=True
            self.direction=3
            self.images=self.imageLeft
        elif event.key == pygame.K_RIGHT:
            self.moving=True
            self.direction=4
            self.images=self.imageRight
        if event.key == pygame.K_UP:
            self.moving=True
            self.direction=1
            self.images=self.imageUp
        elif event.key == pygame.K_DOWN:
            self.moving=True
            self.direction=2
            self.images=self.imageUp
        

    def stopMove(self, event):
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            self.moving=False

    def updateImage(self):
        if self.counter==const.FPS/2:
            self.image=self.images[self.whichImage]
            if self.whichImage==1: 
                self.whichImage=0
            else:
                self.whichImage=1
            self.counter=0

    def actuallyMoving(self):
        if self.moving:
            if self.direction==1:
                self.y-=self.speed
            elif self.direction==2:
                self.y+=self.speed
            elif self.direction==3:
                self.x-=self.speed
            if self.direction==4:
                self.x+=self.speed
            self.counter+=1


    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        self.actuallyMoving()
        
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