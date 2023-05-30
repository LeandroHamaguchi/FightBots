import pygame
from configuracoes import ALTURA,LARGURA,bala_player
from pygame.locals import *


class Foxbot(pygame.sprite.Sprite):
    def __init__(self, img,W,S):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 112.5
        self.rect.bottom = ALTURA/2 +50
        self.speedy = 1
        self.listaBalas=[]
        self.W=W
        self.S=S

    def update(self):
        self.rect.x = 112.5-50
        self.rect.y += self.speedy

            
        #Colisão com a altura
        if self.rect.y > ALTURA-185:
            self.rect.y = ALTURA-185
        if self.rect.y < 85:
            self.rect.y = 85

    def fire(self,x,y):
            Tiro=Bala(x,y,bala_player,self.W,self.S)
            self.listaBalas.append(Tiro)
        

   

class Bala(pygame.sprite.Sprite):
    def __init__(self,posx,posy,imagem,W,S):
        pygame.sprite.Sprite.__init__(self)
        self.listaBalas=[]
        self.ImgBala=pygame.transform.rotate(imagem,-90)
        self.rect = self.ImgBala.get_rect(center=(posx,posy))
        self.speedBala = 3
        self.W=W
        self.S=S

    def percurso(self,imagem):
        if self.W == 1:
            self.rect.x += self.speedBala
        if self.S == 1:
            self.rect.x += self.speedBala
        self.ImgBala=pygame.transform.rotate(imagem,-90)
    def insert(self,superficie):
        superficie.blit(self.ImgBala, self.rect)

