import constants as const
import utility as util
import pygame
import sprites
import playing_music as play

obstacles = pygame.sprite.Group()
height = 100
width =150
#creating obstacles
def create_maze():
    x_Val = 1

 #top
    for i in range(1,12):
        if i!= 13:
            obstacles.add(sprites.Hinder(x_Val,0, width, height, True,0))
        
        x_Val = x_Val +width
#left
y_Val = 2 
for i in range(1, 10):
    if i not in (5, 6):
         obstacles.add(sprites.Hinder(1, y_Val, width, height, True, 0))
    
    y_Val = y_Val + height
  
#bootom
    x_Val = 1
    for i in range(1,12):
        obstacles.add(sprites.Hinder(x_Val,const.HEIGHT - height, width, height, True,0))
        x_Val = x_Val +width
#right
    y_Val = 2 
    for i in range(1, 10):
        if i not in (2,3):
             obstacles.add(sprites.Hinder(const.WIDTH - width, y_Val, width, height, True, 0))
    
        y_Val = y_Val + height
#middle
    for i in (3,5,7,9):
        x_px = i * width
        for j in range(1,8):
           if i == 3 and j in (3, 7): continue
           if i == 5 and j in (4, 5): continue
           if i == 7 and j in (2, 8): continue
           if i == 9 and j == 5: continue
           
           obstacles.add(sprites.Hinder(x_px, j *height, width, height, True, 0))

def playLevel(player):
#     #music
#     play.CurrentPage("other")
   #const.SCREEN.fill("assets\Backround floor2.jpg")
    util.imageToScreen("assets/Backround floor2.jpg", 0, 0,const.WIDTH, const.HEIGHT)
    create_maze()
#    util.imageToScreen("assets\Backround floor2.jpg")
    for obstacle in obstacles:
        obstacle.display()
    door.display()
    player.collisions(obstacles)
    return door.collide(player, 1)

