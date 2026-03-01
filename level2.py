import constants as const
import utility as util
import pygame
import sprites

obstacles = pygame.sprite.Group()
size=50
obstacles.add(sprites.Hinder(10,300, 350, size, False,1, "assets/door.png"))
obstacles.add(sprites.Hinder(450, 700, 350, size, False,1, "assets/door.png"))

#objects
key=sprites.Object(450, 300, 40, 40, "assets/key.png", 1)

background="assets/backround floor2 dark.png"
#new background
def newBackground():
    background="assets/backround floor2 dark.png"


#level
def playLevel(player):
    util.imageToScreen(background, 0, 0,const.WIDTH, const.HEIGHT)

#    util.imageToScreen("assets\Backround floor2.jpg")
    key.display()
    key.collide(player)
    for obstacle in obstacles:
        obstacle.display()
    player.collisions(obstacles)
