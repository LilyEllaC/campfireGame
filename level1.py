import constants as const
import utility as util
import pygame
import sprites
import playing_music as play


#creating obstacles
obstacles=pygame.sprite.Group()
obstacles.add(sprites.Hinder(200, 300, 150, 150, True,0))
obstacles.add(sprites.Hinder(400, 300, 150, 150, True,0))



def playLevel(player):
#     #music
#     play.CurrentPage("other")
   #const.SCREEN.fill("assets\Backround floor2.jpg")
    util.imageToScreen("assets/Backround floor2.jpg", 0, 0,const.WIDTH, const.HEIGHT)

#    util.imageToScreen("assets\Backround floor2.jpg")
    for obstacle in obstacles:
        obstacle.display()
    player.collisions(obstacle)

