import pygame
from foxbot import Foxbot
from configuracoes import ALTURA,LARGURA


foxbot_img_0 = pygame.image.load('assets/foxbot_K_D.png').convert_alpha()
foxbot = Foxbot(foxbot_img_0)



class Bot(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000
        self.rect.bottom = 420
        self.speedx = 10
        self.speedy = 10
        self.direcao="oeste"
    def bussola(self,x_bot, y_bot, x_foxbot, y_foxbot): 
      if ((x_foxbot == x_bot) and (y_foxbot == y_bot)):
        self.direcao= "achou"
      else:
        if (abs(x_foxbot - x_bot) > abs(y_foxbot - y_bot)):
          if (y_foxbot > y_bot):
            self.direcao= "sul"
          elif (y_foxbot < y_bot):
            self.direcao= "norte"
          else: 
            if (x_foxbot > x_bot):
              self.direcao= "leste"
            else:
              self.direcao= "oeste"
        elif (abs(x_foxbot - x_bot) < abs(y_foxbot - y_bot)):
          if (x_foxbot > x_bot):
            self.direcao= "leste"
          elif (x_foxbot < x_bot):
            self.direcao= "oeste"
          else:
            if (y_foxbot > y_bot):
              self.direcao= "sul"
            else:
              self.direcao= "norte"
        else:
          if (y_foxbot > y_bot):
            self.direcao= "sul"
          else:
            self.direcao= "norte"
    def update(self): 
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.direcao == 'norte':
            self.rect.x += 0
            self.rect.y -= self.speedy
        elif self.direcao == 'sul':
            self.rect.x += 0
            self.rect.y += self.speedy 
        elif self.direcao == 'leste':
            self.rect.x += self.speedx
            self.rect.y += 0
        elif self.direcao == 'oeste':
            self.rect.x -= self.speedx
            self.rect.y += 0
        else:
           print('boom')

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        
