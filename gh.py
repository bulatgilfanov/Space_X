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


x = 350
y = 500
speed = 5

clock = pygame.time.Clock()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def floor():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        win.blit("run")

        PLAY_BACK = Button(image=None, pos=(750, 600),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    show_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        win.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(750, 650))
        win.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    show_menu()

        pygame.display.update()

def show_menu():

    while True:
        win.blit(menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()



        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")



        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    floor()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    quit()

        pygame.display.update()

show_menu()


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

def run():

run = True
while(run):
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    list_circles = []

    start_ticks=pygame.time.get_ticks() #starter tick

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
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))
    list_circles.append(Circle(win, color, random.randint(0, 1000), 0))


    player_rect = pygame.Rect((x + 45, y), (90, 60))

    for i in list_circles:
        if player_rect.collidepoint((i.x, i.y)):
            win.blit(lose, (0, 0))
            run = False
        i.draw()
        i.horizontal_movement()



    pygame.display.update()