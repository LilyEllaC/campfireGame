import constants as const
import utility as util
import pygame
import sprites

blindness=sprites.Object(const.WIDTH//2,const.HEIGHT//2,0,0, "assets/ghost sprite (front).png", 0)

obstacles = pygame.sprite.Group()
size=50
obstacles.add(sprites.Hinder(10,300, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(450, 700, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(950, 200, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(1300, 500, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(1100, 500, size, 350, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(230, 600, size, 350, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(800, 50, size, 350, False,0, "assets/backround floor2 dark.png"))


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
    if player.blind:
        blindness.display()
        blindness.width=const.WIDTH
        blindness.height=const.HEIGHT
        

