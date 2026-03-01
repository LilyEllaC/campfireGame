import constants as const
import utility as util
import buttons
import pygame

#getting a button
continueButton=buttons.Button(200, 150, const.WIDTH/2-100, const.HEIGHT-200, const.RED, const.LIGHT_RED)

#intro
def playIntro():
    print("in the intro loop")
    const.SCREEN.fill(const.BLUE)
    util.toScreen("welcome to fliped", const.FONT20, const.RED, const.WIDTH/2, 500)
    util.toScreen("Title", const.FONT200, const.YELLOW, const.WIDTH/2, 100)
    util.imageToScreen("assets/intro_pic.png", const.WIDTH//2 - 250, const.HEIGHT//2 - 250, 500, 500)
    continueButton.display()
    continueButton.checkMouse()