import pygame
from configuracoes import ALTURA,LARGURA,bala_player
from pygame.locals import *


class Foxbot(pygame.sprite.Sprite):
    def __init__(self, img):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = ALTURA/2 +50
        self.speedx = 0
        self.speedy = 0
        self.listaBalas=[]

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Colisão com a largura
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
            
        #Colisão com a altura
        if self.rect.y > ALTURA:
            self.rect.y = ALTURA-90
        if self.rect.y < 0:
            self.rect.y = 0

    def fire(self,x,y):
            Tiro=Bala(x,y,bala_player)
            self.listaBalas.append(Tiro)
        

   

class Bala(pygame.sprite.Sprite):
    def __init__(self,posx,posy,imagem):
        pygame.sprite.Sprite.__init__(self)
        self.listaBalas=[]
        self.ImgBala=pygame.transform.rotate(imagem,-90)
        self.rect = self.ImgBala.get_rect()
        self.speedBala = 1
        self.rect.top = posy
        self.rect.left = posx

    def percurso(self,W,A,S,D,imagem):
        if W == 1:
            self.rect.top = self.rect.top-self.speedBala
            self.ImgBala=imagem
        if S == 1:
            self.rect.top = self.rect.top+self.speedBala
            self.ImgBala=bala_player
        if A == 1:
            self.rect.x -= self.speedBala
            self.ImgBala=pygame.transform.rotate(bala_player,-90)
        if D == 1:
            self.rect.x += self.speedBala
            self.ImgBala=pygame.transform.rotate(bala_player,-90)
    
    def insert(self,superficie):
        superficie.blit(self.ImgBala, self.rect)