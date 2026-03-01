import constants as const
import utility as util
import sprites
import level1
import level2
import level3
import pygame


#create player
player=sprites.Player(30,const.HEIGHT/2,210,210)
level=1


#play
def playGame():
    global level
    if level==1:
        level=level1.playLevel(player)
    elif level==2:
        level=level2.playLevel(player)
    elif level==3:
        level=level3.playLevel(player)
    elif level==4:
        player.x=const.WIDTH-100
        player.y=const.HEIGHT//2
        return "ending"
    else:
        return "Loss"
    return "playing"
    

    
