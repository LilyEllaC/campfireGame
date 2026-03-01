import pygame
import constants as const

#to screen
def toScreen(words, font, colour, x, y):
    text=font.render(words, True, colour)
    textRect=text.get_rect()
    textRect.center=(x,y)
    const.SCREEN.blit(text, textRect)
def toScreen2(words1, words2, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height() // 2)
    toScreen(words2, font, colour, x, y + font.get_height() // 2)
def toScreen3(words1, words2, words3, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height())
    toScreen(words2, font, colour, x, y)
    toScreen(words3, font, colour, x, y + font.get_height())
#images
def imageToScreen(imageName, x, y, width, height):
    image = pygame.image.load(imageName)
    image = pygame.transform.scale(image, (width, height))
    const.SCREEN.blit(image, (x, y))

