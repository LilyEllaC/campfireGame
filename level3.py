import constants as const
import utility as util
import pygame
import sprites

obstacles = pygame.sprite.Group()
size=50
obstacles.add(sprites.Hinder(10,300, 350, size, False,0))
obstacles.add(sprites.Hinder(450, 700, 350, size, False,0))

ghost=sprites.Ghost(const.WIDTH/2, const.HEIGHT/2, 100, 100)

def playLevel(player):
    util.imageToScreen("assets/backround floor2 dark.png", 0, 0,const.WIDTH, const.HEIGHT)
    util.toScreen("Level 3", const.FONT25, const.YELLOW, const.WIDTH-100, 30)

    for obstacle in obstacles:
        obstacle.display()
    player.collisions(obstacles)
    ghost.move(player)
    ghost.collide(player)
    ghost.display()
