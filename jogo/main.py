import pygame
pygame.init()
import foxbot as foxbot
from foxbot import Bala
from tela_inc import game_intro
from configuracoes import *
from pygame.locals import *
clock=pygame.time.Clock()

# classe Bot
class Bala_Bot(pygame.sprite.Sprite):
    def __init__(self,posx,posy,imagem):
        pygame.sprite.Sprite.__init__(self)
        self.listaBalas=[]
        self.ImgBala=pygame.transform.rotate(imagem,-90)
        self.rect = self.ImgBala.get_rect(center=(posx,posy))
        self.speedBala = 3

    def percurso(self):
            self.rect.x -= self.speedBala

    def insert(self,superficie):
        superficie.blit(self.ImgBala, self.rect)

class Bot(pygame.sprite.Sprite):
    
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 887.5
        self.rect.bottom = 420
        self.speedx = 0
        self.speedy = 1
        self.direcao_x=0
        self.direcao_y=0
        self.listaBalas_Inimigo=[]
    def bussola(self,x_bot, y_bot, x_foxbot, y_foxbot): 
        if (y_foxbot > y_bot):
            self.direcao_y= "sul"
        elif (y_foxbot < y_bot):
            self.direcao_y= "norte"
        if (x_foxbot > x_bot):
              self.direcao_x= "leste"
        elif (x_foxbot < x_bot):
              self.direcao_x= "oeste"
        if (x_foxbot > x_bot):
            self.direcao_x= "leste"
        elif (x_foxbot < x_bot):
            self.direcao_x= "oeste"
    def update(self): 
        
        if self.direcao_y == 'norte':
            self.rect.y -= self.speedy      
        if self.direcao_y == 'sul':
            self.rect.y += self.speedy 
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
        # Colisão com a largura
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
            
        # Colisão com a altura
        if self.rect.y > ALTURA:
            self.rect.y = ALTURA-90
        if self.rect.y < 0:
            self.rect.y = 0
    
    def fire(self,x,y):
            Tiro=Bala_Bot(x,y,bala_bot)
            self.listaBalas_Inimigo.append(Tiro)


# spawn do bot + posições iniciais
bot = Bot(bot_img)

# spawn do player
foxbot = foxbot.Foxbot(foxbot_img)

#sprites
sprites = pygame.sprite.Group()
sprites.add(foxbot)
sprites.add(bot)

balaProjetil=Bala(LARGURA / 2 , ALTURA - 60,bala_player)
balaProjetil_Inimigo=Bala_Bot(LARGURA / 2 , ALTURA - 60,bala_bot)


#timer dos tiros do bot
pygame.time.set_timer(pygame.USEREVENT,1000)  # evento a cada 400 milisegundos

# loop principal do jogo
running=True
state= INIT
while state != QUIT:
    if state==INIT:
        state=  game_intro(window)
    elif state==START:
        while running:
            clock.tick(FPS)
            balaProjetil.percurso()
            balaProjetil_Inimigo.percurso()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if running == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running= False
                        if event.key == pygame.K_w:
                            foxbot.speedy -= 4
                            #Foxbot(tecla W)

                        elif event.key == pygame.K_s:
                            foxbot.speedy += 4                    
                            #Foxbot(tecla S)
                        
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w:
                            foxbot.speedy+=4
                            #Foxbot(tecla W)
                        elif event.key == pygame.K_s:
                            foxbot.speedy -=4
                            #Foxbot(tecla S)
  
                    if event.type == MOUSEBUTTONDOWN:
                       x,y = foxbot.rect.center
                       foxbot.fire(x+45,y-5) 


                    if event.type == pygame.USEREVENT:
                        x,y = bot.rect.center                     
                        bot.bussola(bot.rect.x,bot.rect.y,foxbot.rect.x,foxbot.rect.y)
                        bot.fire(x+45,y-5) 
                bot.update()
                foxbot.update()


            window.blit(background, (0, 0))
            sprites.draw(window)
            sprites.draw(window)
            #tiros do jogador
            for x in foxbot.listaBalas:
                    x.insert(window)
                    x.percurso()

            #tiros do bot
            for b in bot.listaBalas_Inimigo:
                    b.insert(window)
                    b.percurso()
            pygame.display.update()

        pygame.quit()
        state=QUIT
    
pygame.quit()
