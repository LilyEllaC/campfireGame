import constants as const
import utility as util
import pygame
import sprites

obstacles = pygame.sprite.Group()
size=50
obstacles.add(sprites.Hinder(10,300, 350, size, False,1))
obstacles.add(sprites.Hinder(450, 700, 350, size, False,1))


def playLevel(player):
    util.imageToScreen("assets/backround floor2 dark.png", 0, 0,const.WIDTH, const.HEIGHT)

#    util.imageToScreen("assets\Backround floor2.jpg")
    for obstacle in obstacles:
        obstacle.display()
    player.collisions(obstacles)
