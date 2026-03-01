import pygame
import utility as util
import constants as const
from game import player
import sprites

image="assets/Intro pg 2.png"
image="assets/real entrance.png"

player.x=const.WIDTH/2-250
player.y=const.HEIGHT-50

#granny
granny=sprites.Granny()
moveOn=False

#show the scene
def showScene():
    global image
    util.imageToScreen(image, 0, 0, const.WIDTH, const.HEIGHT)
    #outside scene
    if player.y>500 and image=="assets/real entrance.png":
        buttonRect=pygame.Rect(const.WIDTH/2-480, 5, 1000, 70)
        pygame.draw.rect(const.SCREEN, const.BLACK, buttonRect)
        util.toScreen2("You are lost. Very lost. Embarrassingly lost.", "Your phone is dead. Your snacks are gone. And something in the bushes has been following you.", const.FONT20, const.RED, const.WIDTH//2, 30)
        player.direction=1
        player.moving=True
        player.images=player.imageUp
        player.rebound=3.5
    elif player.y>497 and image=="assets/real entrance.png":
        util.toScreen("Oh. A house. In the middle of the woods. That's... probably fine.", const.FONT30, const.RED, const.WIDTH//2, 240)
        player.moving=False
        player.y=496
    elif player.y>300 and image=="assets/real entrance.png":
        buttonRect=pygame.Rect(const.WIDTH/2-460, 220, 920, 40)
        pygame.draw.rect(const.SCREEN, const.BLACK, buttonRect)
        util.toScreen("Oh. A house. In the middle of the woods. That's... probably fine.", const.FONT30, const.RED, const.WIDTH//2, 240)
        player.direction=1
        player.moving=True
        player.images=player.imageUp
        player.rebound=2.5
    else:
        image="assets/Intro pg 2.png"
        player.height=150
        player.width=150
        player.resize()
        player.y=600

    #interior
    if image=="assets/Intro pg 2.png":
        buttonRect=pygame.Rect(const.WIDTH/2-100, 150, 855, 100)
        pygame.draw.rect(const.SCREEN, const.BLACK, buttonRect)
        util.toScreen3("Granny: Oh sweetheart, you look terrible"," ","Sit, Sit! I'll make you some tea. I'll be right back, don't touch anything.", const.FONT25, const.RED, const.WIDTH/2+330, 200)
        util.toScreen("She's not wrong.", const.FONT25, const.RED, const.WIDTH/2+330, 200)
        granny.y-=0.5
        if granny.y<340:
            granny.y-=3
        if granny.y>150:
            granny.display()
    player.display()
        
    if moveOn==True:
        return "playing"
    return "introScene"
