import pygame
import time
import foxbot as foxbot
from tela_inc import game_intro
from configuracoes import *
pygame.init()
from pygame.locals import *
from foxbot import Bala

clock=pygame.time.Clock()

FPS= 60



# personagens e classes

listaBalas_Inimigo=[]
listaBalas=[]
#bot loop
class Bot(pygame.sprite.Sprite):
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000
        self.rect.bottom = 420
        self.speedx = 1
        self.speedy = 1
        self.direcao_x=0
        self.direcao_y=0
        self.listaBalas_Inimigo=[]
    def bussola(self,x_bot, y_bot, x_foxbot, y_foxbot): 
        if (abs(x_foxbot - x_bot) > abs(y_foxbot - y_bot)):
          if (y_foxbot > y_bot):
            self.direcao_y= "sul"
          elif (y_foxbot < y_bot):
            self.direcao_y= "norte"
        if (x_foxbot > x_bot):
              self.direcao_x= "leste"
        else:
              self.direcao_x= "oeste"
        if (abs(x_foxbot - x_bot) < abs(y_foxbot - y_bot)):
          if (x_foxbot > x_bot):
            self.direcao_x= "leste"
          elif (x_foxbot < x_bot):
            self.direcao_x= "oeste"
            if (y_foxbot > y_bot):
              self.direcao_y= "sul"
            else:
              self.direcao_y= "norte"
    def update(self): 
        
        if self.direcao_y == 'norte':
            self.rect.y -= self.speedy
            bot.image=pygame.transform.rotate(bot_img,+90)
        elif self.direcao_y == 'sul':
            self.rect.y += self.speedy 
            bot.image=pygame.transform.rotate(bot_img,-90)
        if self.direcao_x == 'leste':
            self.rect.x += self.speedx
            bot.image=pygame.transform.rotate(bot_img,+180)
        elif self.direcao_x == 'oeste':
            self.rect.x -= self.speedx
            bot.image=bot_img

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
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
            Tiro=Bala(x,y,bala_bot)
            self.listaBalas_Inimigo.append(Tiro)

    def direcao(self):
        if self.direcao_y == 'norte':
            self.Wb=1
            self.Sb=0
            self.Db=0
            self.Ab=0
        elif self.direcao_y == 'sul':
            self.Wb=0
            self.Sb=1
            self.Db=0
            self.Ab=0
        if self.direcao_x == 'leste':
            self.Wb=0
            self.Sb=0
            self.Db=1
            self.Ab=0
        elif self.direcao_x == 'oeste':
            self.Wb=0
            self.Sb=0
            self.Db=0
            self.Ab=1


foxbot = foxbot.Foxbot(foxbot_img)
bot = Bot(bot_img)
sprites = pygame.sprite.Group()
sprites.add(foxbot)
sprites.add(bot)
balaProjetil=Bala(LARGURA / 2 , ALTURA - 60,bala_player)
balaProjetil_Inimigo=Bala(LARGURA / 2 , ALTURA - 60,bala_bot)

W=0
S=0
D=1
A=0


bot.Wb=0
bot.Sb=0
bot.Db=1
bot.Ab=0

pygame.time.set_timer(pygame.USEREVENT,400)  # evento a cada 200 milisegundos
# loop principal do jogo
running=True
state= INIT
while state != QUIT:
    if state==INIT:
        state=  game_intro(window)
    elif state==START:
        while running:
            clock.tick(FPS)
            balaProjetil.percurso(W,A,S,D,bala_player )
            balaProjetil_Inimigo.percurso(W,A,S,D,bala_bot)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if running == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running= False
                        if event.key == pygame.K_w:
                            foxbot.speedy = 0
                            foxbot.speedy -= 15
                            foxbot.speedx = 0
                            foxbot.image=pygame.transform.rotate(foxbot_img,+90)
                            foxbot.update()
                            W=1
                            A=0
                            S=0
                            D=0
                            #Foxbot(tecla W)
                        if event.key == pygame.K_s:
                            foxbot.speedy = 0
                            foxbot.speedy += 15
                            foxbot.speedx = 0
                            foxbot.image=pygame.transform.rotate(foxbot_img,-90)
                            foxbot.update()
                            W=0
                            A=0
                            S=1
                            D=0                            
                            #Foxbot(tecla S)
                        if event.key == pygame.K_a:
                            foxbot.speedx = 0
                            foxbot.speedx -= 15
                            foxbot.speedy = 0
                            foxbot.image=pygame.transform.rotate(foxbot_img,-180)
                            foxbot.update()
                            W=0
                            A=1
                            S=0
                            D=0                            
                            #Foxbot(tecla A )
                        if event.key == pygame.K_d:
                            foxbot.speedx = 0
                            foxbot.speedx += 15
                            foxbot.speedy = 0
                            foxbot.image=foxbot_img
                            foxbot.update()
                            W=0
                            A=0
                            S=0
                            D=1
                            #Foxbot(tecla D)
  
                    if event.type == MOUSEBUTTONDOWN:
                       x,y = foxbot.rect.center
                       foxbot.fire(x+45,y-5) 


                    x,y = bot.rect.center                     
                    bot.bussola(bot.rect.x,bot.rect.y,foxbot.rect.x,foxbot.rect.y)
                    if event.type == pygame.USEREVENT:
                        
                        bot.fire(x+45,y-5) 
                        bot.direcao()
                bot.update()


            window.blit(background, (0, 0))
            sprites.draw(window)
            sprites.draw(window)
            #tiros do jogador
            if len(foxbot.listaBalas) > 0:
                for x in foxbot.listaBalas:
                    x.insert(window)
                    x.percurso(W,A,S,D,bala_player)

            #tiros do bot
            if len(bot.listaBalas_Inimigo) > 0:
                for b in bot.listaBalas_Inimigo:
                    b.insert(window)
                    b.percurso(bot.Wb,bot.Ab,bot.Sb,bot.Db,bala_bot)
            pygame.display.update()

        pygame.quit()
        state=QUIT
    
pygame.quit()
