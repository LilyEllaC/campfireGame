import pygame
import utility as util
import constants as const
import intro
import game
import level2
import level1
import ending
import introScene
import sprites
import asyncio

# pylint: disable=no-member

pygame.init()

#variables
running=True
clock=pygame.time.Clock()
pygame.display.set_caption("Campfire Game")

#moving through scenes


#main
async def main():
    global running
    gameState="introScene"

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if gameState=="introScene":
                if event.type==pygame.KEYDOWN:
                    if introScene.granny.y<150:
                        introScene.moveOn=True
                        game.player.rebound=5
                        gameState="playing"
            if gameState=="playing":
                if event.type==pygame.KEYDOWN:
                    game.player.move(event)
                if event.type==pygame.KEYUP:
                    game.player.stopMove(event)
                if game.level==2:
                    if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                        level2.newBackground()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        for obstacle in level2.obstacles:
                            if obstacle.rect.collidepoint(event.pos):
                                obstacle.move()

            if gameState=="intro":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if intro.continueButton.colour==intro.continueButton.colourOn:
                        gameState="playing"
        
        #different settings
        if gameState=="intro":
            intro.playIntro()
        elif gameState=="introScene":
            gameState=introScene.showScene()
        elif gameState=="playing":
            gameState=game.playGame()
        elif gameState=="ending":
            ending.showEnd()
        #util.toScreen("FPS: "+str(clock.get_fps()), const.FONT30,const.RED, 1000, 10)
        #end
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(const.FPS)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()

