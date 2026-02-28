import constants as const
import utility as util
import buttons

#getting a button
continueButton=buttons.Button(200, 150, const.WIDTH/2-100, const.HEIGHT-200, const.RED, const.LIGHT_RED)

#intro
def playIntro():
    const.SCREEN.fill(const.BLUE)
    util.imageToScreen("assets/intro.png", const.WIDTH, const.HEIGHT, 500, 500)
    util.toScreen("welcome to fliped", const.FONT20, const.RED, const.WIDTH/2, 500)
    util.toScreen("Title", const.FONT200, const.YELLOW, const.WIDTH/2, 100)
    continueButton.display()
    continueButton.checkMouse()