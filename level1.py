import constants as const
import utility as util
import pygame
import sprites
import playing_music as play


#creating obstacles
obstacles=pygame.sprite.Group()
obstacles.add(sprites.Hinder(200, 300, 50, 50, True,0))



def playLevel():
    #music
    play.CurrentPage("other")
    const.SCREEN.fill(const.ORANGE)
    obstacles.draw(const.SCREEN)

