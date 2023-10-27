import pygame

pygame.init()
win = pygame.display.set_mode((2000, 1500))
pygame.mixer.music.load("sound/orange.mp3")
screamer = pygame.image.load("fon/bruh.jpg")
screamer_size = (2000, 1500)
screamer = pygame.transform.scale(screamer, (screamer_size[0], screamer_size[1]))


def screamer():
    win.blit(screamer(0, 0))

