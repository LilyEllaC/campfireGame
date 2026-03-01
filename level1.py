import constants as const
import utility as util
import pygame
import sprites
import playing_music as play

obstacles = pygame.sprite.Group()
size = 50
#creating obstacles
def create_maze():
 #top

    obstacles.add(sprites.Hinder(0,0, 350, size, True,0))
    obstacles.add(sprites.Hinder(450, 0, 350, size, True,0))

    #bootom
    obstacles.add(sprites.Hinder(0, const.HEIGHT - W, 350, W, True, 0))
    obstacles.add(sprites.Hinder(450, const.HEIGHT - W, 350, W, True, 0))

    #side
    obstacles.add(sprites.Hinder(0, 0,w,const.HEIGHT,True, 0))
    obstacles.add(sprites.Hinder(const.WIDTH - W, 0, W, const.HEIGHT, True, 0))



def playLevel(player):
#     #music
#     play.CurrentPage("other")
   #const.SCREEN.fill("assets\Backround floor2.jpg")
    util.imageToScreen("assets/Backround floor2.jpg", 0, 0,const.WIDTH, const.HEIGHT)

#    util.imageToScreen("assets\Backround floor2.jpg")
    for obstacle in obstacles:
        obstacle.display()
    player.collisions(obstacles)

