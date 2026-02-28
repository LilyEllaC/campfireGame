import pygame
import utility as util
import constants as const
import asyncio
# pylint: disable=no-member

pygame.init()

#variables
running=True
clock=pygame.time.Clock()
pygame.display.set_caption("Campfire Game")



async def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        const.SCREEN.fill(const.BLACK)
        util.toScreen("Hi", const.FONT20, const.RED, 500,500)
        
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(const.FPS)

if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()

