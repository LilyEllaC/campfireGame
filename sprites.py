import pygame
import constants as const
import utility as util
import random

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


        #moving and hitbox
        self.normRect = self.image.get_rect()
        self.rect=self.normRect.inflate(-65,-20)
        self.offSetX=30
        self.offSetY=15
        self.rect.x= x+self.offSetX
        self.rect.y = y+self.offSetY

        #collisions
        self.speed=10
        self.moving=False
        self.rebound=5

        #blindness
        self.blind=False
        self.blindTimer=0

        #appearance
        self.direction=1
        self.whichImage=1
        self.counter=0
        self.imageRight=[pygame.transform.scale(pygame.image.load("assets/playerRight1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]#, pygame.transform.scale(pygame.image.load("assets/playerRight1.png"),(width, height))]#[pygame.transform.scale(pygame.image.load("assets/playerRight1"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]
        self.imageLeft=[pygame.transform.scale(pygame.image.load("assets/playerLeft1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerLeft2.png"),(width, height))]#[pygame.transform.scale(pygame.image.load("assets/playerLeft1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerRight2.png"),(width, height))]
        self.imageUp=[pygame.transform.scale(pygame.image.load("assets/playerUp.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerUp.png"),(width, height))]
        self.imageDown=[pygame.transform.scale(pygame.image.load("assets/playerDown1.png"),(width, height)), pygame.transform.scale(pygame.image.load("assets/playerDown2.png"),(width, height))]
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
            self.images=self.imageDown
        self.counter=15
        
    def stopMove(self, event):
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            self.moving=False

    def updateImage(self):
        if self.counter>const.FPS/4:
            self.image=self.images[self.whichImage]
            if self.whichImage==1: 
                self.whichImage=0
            else:
                self.whichImage=1
            self.counter=0

    def actuallyMoving(self):
        self.rect.x=self.x+self.offSetX
        self.rect.y=self.y+self.offSetY
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
            
            self.updateImage()


    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        self.actuallyMoving()
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)

    
    def collisions(self, obstacles):
        collided=pygame.sprite.spritecollide(self, obstacles, False)
        if collided:
            for collider in collided:
                if collider.isPainful:
                    self.x=0
                    self.y=const.HEIGHT/2+90
                else:
                    if self.direction==1:
                        self.y+=self.speed
                    elif self.direction==2:
                        self.y-=self.speed
                    elif self.direction==3:
                        self.x+=self.speed
                    if self.direction==4:
                        self.x-=self.speed


class Hinder(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, isPainful, moveDirection, image):
        super().__init__()
        if isPainful:
            self.imageType=pygame.image.load("assets/replace.png")
            self.altImage=pygame.image.load("assets/replace.png")
        else: 
            if image=="assets/door.png":
                self.altImage=pygame.image.load("assets/table sprite dark.png")
            else:
                self.altImage=pygame.image.load(image)
            self.imageType=pygame.image.load(image)
            self.imageNum=0


        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.imageType, (self.width, self.height))

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
                    self.yAddition=10


    def changeMode(self):
        if self.imageNum==0:
            self.image=pygame.transform.scale(self.altImage, (self.width, self.height))
            self.imageNum=1
        else:
            self.image=pygame.transform.scale(self.imageType, (self.width, self.height))
            self.imageNum=0

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
            if not (self.moveDirect==1 and self.y>self.endPos) or (self.moveDirect==2 and self.y<self.endPos) or (self.moveDirect==3 and self.x>self.endPos) or (self.moveDirect==4 and self.x<self.endPos):
                self.moving=False
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.imageType=pygame.image.load("assets/door.png")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.imageType, (width, height))

        self.rect = self.image.get_rect()
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)
        self.rect.x = x
        self.rect.y = y

    def collide(self, player, level):
        if self.rect.colliderect(player.rect):
            level+=1
        return level
    
    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, position):
        super().__init__()
        self.imageType=pygame.image.load(image)
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.imageType, (width, height))
        self.position=position

        self.rect = self.image.get_rect()
        pygame.draw.rect(const.SCREEN, const.BLACK, self.rect, 3)
        self.rect.x = x
        self.rect.y = y

    def collide(self, player):
        if self.rect.colliderect(player.rect):
            print("Gotten")
            self.x=30*self.position
            self.y=30
    
    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        image=pygame.image.load("assets/eyeball sprite (dark).png")
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.speed=2.5
        self.image = pygame.transform.scale(image, (width, height))
        self.xMove=False
        self.yMove=False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, player):
        #having it not bounce like crazy when it is near correct
        if abs(self.x-player.x)>30:
            if self.x+self.width/2>player.x+player.width/2:
                self.x-=self.speed
            else:
                self.x+=self.speed
            self.xMove=True
            self.rect.x=self.x
            self.rect.y=self.y
        else:
            self.xMove=False
        
        #having it not bounce like crazy when it is near correct
        if abs(self.y-player.y)>30:
            if self.y+self.height/2>player.y+player.height/2:
                self.y-=self.speed
            else:
                self.y+=self.speed
            self.yMove=True
        else:
            self.yMove=False
        
        #slowing down on diagonals
        if self.xMove and self.yMove:
            self.speed=1.75
        else:
            self.speed=2.5

    def collide(self, player):
        if self.rect.colliderect(player.rect):
            player.blind=True
            self.x=random.randint(0, const.WIDTH)
            self.y=random.randint(0, const.HEIGHT)

    def display(self):
        const.SCREEN.blit(self.image, (self.x, self.y))
