import pygame

ALTURA = 500
LARGURA = 850

class Foxbot(pygame.sprite.Sprite):
    def __init__(self, img):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - 440
        self.rect.bottom = ALTURA / 2
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
