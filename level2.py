import constants as const
import utility as util
import pygame
import sprites

obstacles = pygame.sprite.Group()
items = pygame.sprite.Group()
size=50

def createObjects():
    obstacles.empty()
    items.empty()
    
 
    # items
    # Clock item Bottom middle)]
    items.add(sprites.Object(const.WIDTH//2 - 20, const.HEIGHT - size*3, 40, 40, "assets/clock sprite (dark).png", 1))
    # Tomato item Top right
    items.add(sprites.Object(const.WIDTH - size*8, size * 2, 40, 40, "assets/tomato sprite dark.png", 2))
    # Key item Bottom right 
    items.add(sprites.Object(size * 16, const.HEIGHT - size*3, 40, 40, "assets/clock sprite (dark).png", 3)) 
    
    # Eyeball Top left 
    items.add(sprites.Object(size * 2, size * 2, 40, 40, "assets/eyeball sprite (dark).png",4))
   
   # Grandfather clock Top middle
    obstacles.add(sprites.Hinder(const.WIDTH//2 - size//2, size * 2, size, size*4, False, 2, "assets/Object_grandfatherclock_sprite_(dark).png"))
    # Chest/Drawers Bottom right
    obstacles.add(sprites.Hinder(size * 15, const.HEIGHT - size*5, size*4, size*3, False, 4, "assets/table sprite dark.png"))
    

    door = sprites.Door(const.WIDTH - size, const.HEIGHT // 2, size, size*2)

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
    
   
        
    if background =="assets/backround floor2 dark.png":
        for item in items:
            item.display()
            item.collide(player)

    if background =="assets/backround floor2 dark.png":
       for obstacle in obstacles:
           obstacle.display()
     
        
    
