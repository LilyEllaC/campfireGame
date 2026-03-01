import constants as const
import utility as util
import buttons
import pygame


#getting a button
continueButton=buttons.Button(200, 150, const.WIDTH/2-100, const.HEIGHT-200, const.RED, const.LIGHT_RED)

#intro
def playIntro():
    #const.SCREEN.fill(const.BLUE)
    util.imageToScreen("assets/intro_pic.png", 0, 0,const.WIDTH, const.HEIGHT)
    continueButton.display()
    continueButton.checkMouse()
    util.toScreen("FLIPPED", const.customFont(210), const.YELLOW, const.WIDTH/2, 100)
    rect=pygame.Rect(270,380,1050,100)
    square=pygame.draw.rect(const.SCREEN, const.BLACK, rect)
    
    util.toScreen("welcome to flipped, you were lost at the forest and stumbled upon this house", const.customFont(35), const.WHITE, const.WIDTH/2, 400)
    util.toScreen("NOW GO INSIDE THE HOUSE", const.customFont(50), const.WHITE, const.WIDTH/2, 450)

#music
pygame.mixer.init()
pygame.mixer.music.load("Music/intro_Music.mp3")
pygame.mixer.music.play(-1)