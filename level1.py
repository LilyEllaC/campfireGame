import constants as const
import utility as util
import pygame
import sprites
import playing_music as play

obstacles = pygame.sprite.Group()
height = 100
door = None
width = 150

def val(x,y,w,h):
    return sprites.Door(x,y,w,h)


# creating obstacles
def create_maze():
    global door
    obstacles.empty()
    x_Val = 1

    # top
    for i in range(1, 12):
        obstacles.add(sprites.Hinder(x_Val, 0, width, height, True, 0, "n"))
        x_Val = x_Val + width

    # left 
    y_Val = height 
    for i in range(1, 10):
        if i not in (5, 6):
            obstacles.add(sprites.Hinder(1, y_Val, width, height, True, 0, "n"))
        y_Val = y_Val + height 
  
    # bottom
    x_Val = 1
    for i in range(1, 12):
        obstacles.add(sprites.Hinder(x_Val, const.HEIGHT - height, width, height, True, 0, "n"))
        x_Val = x_Val + width

    # right 
    y_Val = height 
    for i in range(1, 10):
       
        if i not in (2, 3, 8):
            obstacles.add(sprites.Hinder(const.WIDTH - width, y_Val, width, height, True, 0, "n"))
        
        #door
        if i == 2:
            door=val(const.WIDTH - width, y_Val, width, height*2)

        y_Val = y_Val + height
        
    # middle 
    for i in (3, 5, 7):
        x_px = i * width
        for j in range(1, 10):
            if i == 3 and j in (3,4): continue
            if i == 5 and j in (4, 5): continue
            if i == 7 and j in (2, 3): continue
            
            obstacles.add(sprites.Hinder(x_px, j * height, width, height, True, 0, "n"))

# Initialize objects
# door=sprites.Door(const.WIDTH//2-350, const.HEIGHT/2-50, 150, 300)
key=sprites.Object(const.WIDTH-200, const.HEIGHT-170, 40, 40, "assets/key.png", 1)
create_maze()

def playLevel(player):
    util.imageToScreen("assets/Backround floor2.jpg", 0, 0, const.WIDTH, const.HEIGHT)
    global door
    for obstacle in obstacles:
        obstacle.display()
    #if door is not None:
    door.display()
    
    player.collisions(obstacles)

    player.display()
    player.updateImage()   
    key.display()
    key.collide(player) 

    #text


    #if door:
    if key.y==30:
        rect=pygame.Rect(const.WIDTH/2-480, 5, 1000, 70)
        square=pygame.draw.rect(const.SCREEN, const.BLACK, rect)
        util.toScreen("Got it. Now get to the door", const.FONT30, const.WHITE, const.WIDTH//2, 20)
        return door.collide(player,1)
    else:
        rect=pygame.Rect(const.WIDTH/2-480, 5, 1000, 70)
        square=pygame.draw.rect(const.SCREEN, const.BLACK, rect)
        util.toScreen2("It's a maze. Somewhere in here is a key. You need the key.", "Start walking, but don't touch the walls.", const.FONT30, const.WHITE, const.WIDTH//2, 40)


    return 1