import pygame

ALTURA = 500
LARGURA = 500

class Foxbot(pygame.sprite.Sprite):
    def __init__(self, img):
        self.img = img
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA - 480
        self.rect.bottom = ALTURA / 2
        self.speedx = 10
        self.speedy = 10

    def update(self, new_speedx, new_speedy):
        self.speedx = new_speedx
        self.speedy = new_speedy
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        
        return self.img
