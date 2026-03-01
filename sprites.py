import pygame
import constants as const
import utility as util

# pylint: disable=no-member

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        image=pygame.image.load("assets/playerUp.png")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y = y
        self.speed=10
        self.moving=False
        self.rebound=5


        self.direction=1
        self.whichImage=1
        self.counter=0
        self.imageRight=[pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]#, pygame.transform.scale(pygame.image.load("assets/playerRight1.png"),(width, height))]#[pygame.transform.scale(pygame.image.load("assets/playerRight1"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]
        self.imageLeft=[pygame.transform.scale(pygame.image.load("assets/playerLeft2.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerLeft2.png"),(width, height))]#[pygame.transform.scale(pygame.image.load("assets/playerLeft1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]
        self.imageUp=[pygame.transform.scale(pygame.image.load("assets/playerUp.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerUp.png"),(width, height))]
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
        self.counter=15
        
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
                self.y-=self.rebound
            elif self.direction==2:
                self.y+=self.rebound
            elif self.direction==3:
                self.x-=self.rebound
            if self.direction==4:
                self.x+=self.rebound
            self.counter+=1
            self.rect.x=self.x
            self.rect.y=self.y


    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        self.actuallyMoving()
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)

    
    def collisions(self, obstacles):
        playerRect=self.image.get_rect()
        if pygame.sprite.spritecollide(self, obstacles, False):
            #if obstacle.isPainful:
                #self.x=0
                #self.y=0
            if True:
                if self.direction==1:
                    self.y+=self.speed
                elif self.direction==2:
                    self.y-=self.speed
                elif self.direction==3:
                    self.x+=self.speed
                if self.direction==4:
                    self.x-=self.speed


class Hinder(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, isPainful, moveDirection):
        super().__init__()
        if isPainful:
            self.imageType=pygame.image.load("assets/obsticle_sprite.png")
            self.altImage=pygame.image.load("assets/obsticle_sprite.png")
        else: 
            self.imageType=pygame.image.load("assets/door.png")
            self.altImage=pygame.image.load("assets/door.png")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.imageType, (width, height))

        self.rect = self.image.get_rect()
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)
        self.rect.x = x
        self.rect.y = y
        self.isPainful=isPainful
        #moving
        self.moveDirect=moveDirection
        self.moving=False
        if self.moveDirect!=0:
            if self.moveDirect>2:
                self.startPos=self.x
                self.yAddition=0
                if self.moveDirect==3:
                    self.endPos=self.startPos-self.width
                    self.xAddition=-10
                if self.moveDirect==4:
                    self.endPos=self.startPos+self.width
                    self.xAddition=10
            else:
                self.startPos=self.y
                self.xAddition=0
                if self.moveDirect==1:
                    self.endPos=self.startPos-self.height
                    self.yAddition=-10
                if self.moveDirect==2:
                    self.endPos=self.startPos+self.height
                    self.xAddition=10


    def changeMode(self):
        if self.image==pygame.transform.scale(self.imageType, (self.width, self.height)):
            self.image=pygame.transform.scale(self.altImage, (self.width, self.height))
        else:
            self.image=pygame.transform.scale(self.imageType, (self.width, self.height))

    def move(self):
        if (self.moveDirect==1 and self.y>self.endPos) or (self.moveDirect==2 and self.y<self.endPos) or (self.moveDirect==3 and self.x>self.endPos) or (self.moveDirect==4 and self.x<self.endPos):
            self.moving=True
        else:
            self.moving=False
            

    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        if self.moving==True:
            self.x+=self.xAddition
            self.y+=self.yAddition
            self.rect.x = self.x
            self.rect.y = self.y
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)



