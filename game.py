import constants as const
import utility as util
import sprites
import level1
import level2
import level3
import pygame


#create player
player=sprites.Player(300,300,200,200)
level=1


#play
def playGame():
    if level==1:
        level1.playLevel(player)
    elif level==2:
        level2.playLevel()
    elif level==3:
        level3.playLevel()
    player.display()
    player.updateImage()

    
