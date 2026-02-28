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
gameState="intro"


#main
async def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.BUTTONDOWN:
                if gameState=="playing":
                    game.player.move()
        
        #different settings
        if gameState=="intro":
            intro.playIntro()

        #end
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(const.FPS)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()

