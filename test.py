background = pygame.image.load("fon/space.jpg")
background_rect = background.get_rect()
player_img = pygame.image.load("sprites/ship.jpg")
meteor_img = pygame.image.load("sprites/meteorBrown.png")
bullet_img = pygame.image.load("sprites/laserRed.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(player_img, (50, 38))
