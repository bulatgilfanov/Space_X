import pygame


pygame.init()
win = pygame.display.set_mode((1000, 700))

clock = pygame.time.Clock()
menu = pygame.image.load("fon/menu.jpg")
button_sound = pygame.mixer.Sound("sound/click.mp3")



def start_game():

    run = True
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



def show_menu():




    show = True
    while show:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


show_menu()

    win.blit(menu, (0, 0))


    pygame.display.update()
    clock.tick(60)


show_menu()