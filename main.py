import pygame
import random

pygame.init()
win = pygame.display.set_mode((1500, 1000))

pygame.mixer.music.load("sound/Vandeta.mp3")
pygame.mixer.music.play(-1)
lose = pygame.image.load("fon/lose.jpg")
lose_size = (1500, 1000)
lose = pygame.transform.scale(lose, (lose_size[0], lose_size[1]))
menu = pygame.image.load("fon/menu.jpg")
player = pygame.image.load("sprites/ship.png")
player_size = (250,250)
player = pygame.transform.scale(player, (player_size[0], player_size[1]))
background = pygame.image.load("fon/space.jpg")
button_sound = pygame.mixer.Sound("sound/click.mp3")
enemy = pygame.image.load("sprites/meteorBrown.png")
enemy_size = (100, 100)
enemy = pygame.transform.scale(enemy, (enemy_size[0], enemy_size[1]))


x = 650
y = 700
speed = 5

clock = pygame.time.Clock()

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def start_game():

    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

class Button():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (13, 162, 58)
        self.active_clr = (23, 204, 58)

    def draw(self, x, y, message, action=None, font_size = 30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(win, self.active_clr, (x, y, self.width, self.height))

            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    action()
        else:
            pygame.draw.rect(win, self.inactive_clr, (x, y, self.width, self.height))

        print_text(message=message, x=x+10, y=-y+10, font_size=font_size)



class Circle():
    def __init__(self, win, color, x, y):
        self.win = win
        self.color = color
        self.x = x
        self.y = y
        self.vel = 5
        self.dir = 'right'

    def draw(self):
        self.win.blit(enemy, (self.x, self.y))

    def horizontal_movement(self):
        self.y += self.vel

def print_text(message, x, y, font_color=(0, 0, 0), font_type='font.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message,True, font_color)
    win.blit(text, (x, y))

list_circles = []

start_ticks=pygame.time.get_ticks() #starter tick


def show_menu():

    start_btn = Button(300, 70)

    show = True
    while show:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    win.blit(menu, (0, 0))
    start_btn.draw(300, 200, "Start game", start_game, 50)

    pygame.display.update()
    clock.tick(60)





run = True
while(run):


    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    win.blit(background, (0, 0))



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed



    win.blit(player,( x, y))

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    if seconds > 2:
        start_ticks = pygame.time.get_ticks()  # starter tick




        color = random.choices(range(256), k=3)
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))
        list_circles.append(Circle(win, color, random.randint(0, 1500), 0))



    player_rect = pygame.Rect((x + 45, y), (90, 60))

    for i in list_circles:
        if player_rect.collidepoint((i.x, i.y)):
            win.blit(lose, (0, 0))
            run = False
        i.draw()
        i.horizontal_movement()



    pygame.display.update()

