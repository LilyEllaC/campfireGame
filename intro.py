import constants as const
import utility as util



#intro
def playIntro():
    const.SCREEN.fill(const.BLACK)
    util.toScreen("Hi", const.FONT20, const.RED, 500,500)
    util.toScreen("Title", const.FONT40, const.YELLOW, const.WIDTH/2, const.HEIGHT/2)