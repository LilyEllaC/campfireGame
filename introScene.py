import pygame
import utility as util
import constants as const
from game import player

#show the scene
def showScene():
    util.imageToScreen("assets/Intro pg 2.png", 0, 0, const.WIDTH, const.HEIGHT)
    util.toScreen("LORE", const.FONT20, const.BLUE, const.WIDTH//2, 30)
    player.display()
