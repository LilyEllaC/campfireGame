import constants as const
import utility as util
import pygame
import sprites
import playing_music as play


obstacles = pygame.sprite.Group()
items = pygame.sprite.Group()
size=50

def createObjects():
    obstacles.empty()
    items.empty()
    
 
    # items
    #x, y, width, height, image, position
    # Clock item Bottom middle)]
    items.add(sprites.Object(500,700, size, size, "assets/clock sprite (dark).png", 1))
    # Tomato item behind sofa
    items.add(sprites.Object(const.WIDTH - size*8, size * 2, size, size, "assets/tomato sprite dark.png", 2))
    # Key item behind table 
    items.add(sprites.Object(1270,const.HEIGHT - size*3, size, size, "assets/key.png", 3)) 
    # Eyeball Top left behind tall clock
    items.add(sprites.Object(const.WIDTH//2-size*3, size*1, size, size, "assets/eyeball sprite (dark).png",4))
   
   #move
   #x, y, width, height, isPainful, moveDirection, image
   # Grandfather clock Top middle
    obstacles.add(sprites.Hinder(const.WIDTH//2-size*4, size//2*1 , size*2, size*7, False, 2, "assets/Object_grandfatherclock_sprite_(dark).png"))
    # Chest/Drawers Bottom right
    obstacles.add(sprites.Hinder(1225, const.HEIGHT - size*5, size*6, size*6, False, 4, "assets/table sprite dark.png"))
    #chair top right
    obstacles.add(sprites.Hinder(1100,size, size*5, size*5, False, 3, "assets/couch (dark).png"))
    #office table
    obstacles.add(sprites.Hinder(300,600, size*5, size*5, False, 4, "assets/Computer (dark).png"))


    
door = sprites.Door(1395,size-35, 200, 300)

background="assets/newLevel2Background1.png"
#new background
def newBackground():
    global background
    
    background="assets/backround floor2 dark.png"
    for obstacle in obstacles:
        obstacle.changeMode()
        
createObjects()

#level
def playLevel(player):
    global background
    util.imageToScreen(background, 0, 0,const.WIDTH, const.HEIGHT)
#     util.imageToScreen("assets\Backround floor2.jpg",)
    door.display()

   
        
    if background =="assets/backround floor2 dark.png":
        for item in items:
            item.display()
            item.collide(player)
            
    if background =="assets/backround floor2 dark.png":
       for obstacle in obstacles:
           player.collisions(obstacles)
           obstacle.display()
            
    for item in items:
        if item.position == 30:
                return door.collide(player, 2)

#      
# =======
#            obstacle.display()
#     player.display()
#     player.updateImage()
# >>>>>>> 7e56453eb00681dde70cc4785ccfd19f21a355b7
#         
    
