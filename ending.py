import pygame
import utility as util
import constants as const
from game import player

#show the scene
def showEnd():
    util.imageToScreen("assets/ending backround.png", 0, 0, const.WIDTH, const.HEIGHT)
    util.toScreen("YOU ESCAPED!!", const.FONT200, const.RED, const.WIDTH//2, 110)

    if player.x>300:
        player.direction=3
        player.moving=True
        player.images=player.imageLeft
        player.speed=5
    elif player.y>300:
        util.toScreen("Next time go sleep in the woods", const.FONT60, const.BLUE, const.WIDTH//2, 240)
        player.direction=1
        player.images=player.imageUp
    else:
        util.toScreen("Next time go sleep in the woods", const.FONT60, const.BLUE, const.WIDTH//2, 240)
        player.moving=False
    player.updateImage()
    player.actuallyMoving()
    player.display()
