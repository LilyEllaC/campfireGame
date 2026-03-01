import pygame
import utility as util
import constants as const
import intro
import game
import ending
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
    gameState="intro"

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if gameState=="playing":
                    game.player.move()

            if gameState=="intro":
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if intro.continueButton.colour==intro.continueButton.colourOn:
                        gameState="playing"
        
        #different settings
        if gameState=="intro":
            intro.playIntro()
        elif gameState=="playing":
            game.playGame()

        #end
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(const.FPS)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()

