import constants as const
import utility as util
import pygame
import sprites

blindness=sprites.Object(0+const.WIDTH/6,0,const.WIDTH/3*2, const.HEIGHT, "assets/ghost sprite (front).png", 0)

obstacles = pygame.sprite.Group()
size=50
obstacles.add(sprites.Hinder(10,300, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(450, 700, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(950, 200, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(1300, 500, 350, size, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(1100, 500, size, 350, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(230, 600, size, 350, False,0, "assets/backround floor2 dark.png"))
obstacles.add(sprites.Hinder(800, 50, size, 350, False,0, "assets/backround floor2 dark.png"))

#items
key=sprites.Object(const.WIDTH-150, const.HEIGHT-100, 40, 40, "assets/key.png", 1)
door = sprites.Door(const.WIDTH - size, const.HEIGHT // 2-200, 150, 300)
ghost=sprites.Ghost(const.WIDTH/2, const.HEIGHT/2, 100, 100)

#clock
timeLeft=90

#playing
def playLevel(player):
    global timeLeft
    util.imageToScreen("assets/backround floor2 dark.png", 0, 0,const.WIDTH, const.HEIGHT)

    #clock
    timeLeft-=1/const.FPS
    util.toScreen("Seconds Left: "+str(round(timeLeft)), const.FONT25, const.RED, const.WIDTH-200, 30)

    #obstacles
    for obstacle in obstacles:
        obstacle.display()
    player.collisions(obstacles)

    #ghost
    ghost.move(player)
    ghost.collide(player)
    ghost.display()
    
    #person
    player.display()
    player.updateImage()
    #blind
    if player.blind:
        player.blindTimer+=1
        blindness.display()
        if player.blindTimer>5*const.FPS:
            player.blind=False
    
    #key
    key.display()
    key.collide(player)
    #door
    door.display()
    if timeLeft<0:
        return 5
    
    #text
    if key.y==30:
        util.toScreen("You have the key, you have two legs, please use both.", const.FONT30, const.RED, const.WIDTH//2, 40)
        return door.collide(player,3)
    else:
        util.toScreen2("Something is already in here with you.", "\"Yup, Run\"", const.FONT30, const.RED, const.WIDTH//2, 40)

    return 3
        

