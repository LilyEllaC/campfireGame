import constants as const
import pygame


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
        self.triangleP1X=self.x+self.width/2*5
        self.triangleP1Y=self.y+self.height/8
        self.triangleP2X=self.x+self.width/2*5
        self.triangleP2Y=self.y+self.height/7*8
        self.triangleP3X=self.x+self.width/3*5
        self.triangleP3Y=self.y+self.height/2
        self.trainglePoints=[(self.traingleP1X, self.triangleP1Y), (self.traingleP2X, self.triangleP2Y), (self.traingleP3X, self.triangleP3Y)]

    def display(self):
        self.button=pygame.draw.rect(const.SCREEN, self.colour, self.buttonRect)

    def checkMouse(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        if (mouseX<=self.x+self.width and mouseX>=self.x) and (mouseY<=self.y+self.height and mouseY>=self.y):
            self.colour=self.colourOn
        else:
            self.colour=self.colourOff
        





