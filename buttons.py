import constants as const
import pygame
import level1 as L_1


class Button:
    def __init__(self, width, height, x, y, colour1, colour2):
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.colourOff=colour1
        self.colourOn=colour2
        self.colour=colour1
        self.buttonRect=pygame.Rect(x, y, width, height)
        self.button=pygame.draw.rect(const.SCREEN, self.colour, self.buttonRect)
        pygame.draw.rect(const.SCREEN, const.BLACK, self.buttonRect, 3)

        self.triangleP1X=self.x+self.width/7*2
        self.triangleP1Y=self.y+self.height/8
        self.triangleP2X=self.x+self.width/7*2
        self.triangleP2Y=self.y+self.height/8*7
        self.triangleP3X=self.x+self.width/7*5
        self.triangleP3Y=self.y+self.height/2
        self.trianglePoints=[(self.triangleP1X, self.triangleP1Y), (self.triangleP2X, self.triangleP2Y), (self.triangleP3X, self.triangleP3Y)]
        pygame.draw.polygon(const.SCREEN, const.BLACK, self.trianglePoints)


    def display(self):
        self.button=pygame.draw.rect(const.SCREEN, self.colour, self.buttonRect)
        pygame.draw.polygon(const.SCREEN, const.BLACK, self.trianglePoints)
        pygame.draw.rect(const.SCREEN, const.BLACK, self.buttonRect, 3)

    def checkMouse(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        if (mouseX<=self.x+self.width and mouseX>=self.x) and (mouseY<=self.y+self.height and mouseY>=self.y):
            self.colour=self.colourOn
        else:
            self.colour=self.colourOff
        





