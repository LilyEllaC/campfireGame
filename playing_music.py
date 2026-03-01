import pygame

pygame.init()
pygame.mixer.init()

#currently playing
current_track = None

def CurrentPage(page):
    global current_track
    if page == "intro" and current_track != "intro":

        try:
            pygame.mixer.music.load("Music/intro_Music.mp3")
            pygame.mixer.music.play(-1)
            current_track = "intro"
        except Exception as e:
            print("Error")
    if page == "other" and current_track != "other":
        try:
            pygame.mixer.music.load("Music/Level1.mp3")
            pygame.mixer.music.play(-1)
            current_track = "other"
        except Exception as e:
            print("Error")