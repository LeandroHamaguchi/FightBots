import pygame
import foxbot as foxbot
import bot as bot
from tela_inc import game_intro
from configuracoes import *
pygame.init()
from pygame.locals import *
from foxbot import Bala
# personagens e classes
foxbot = foxbot.Foxbot(foxbot_img)
bot = bot.Bot(bot_img_0)
sprites = pygame.sprite.Group()
sprites.add(foxbot)
sprites.add(bot)
balaProjetil=Bala(LARGURA / 2 , ALTURA - 60)
listaBalas=[]
W=0
A=0
S=0
D=1

# loop principal do jogo
running=True
state= INIT
while state != QUIT:
    if state==INIT:
        state=  game_intro(window)
    elif state==START:
        while running:
            balaProjetil.percurso(W,A,S,D )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if running == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.QUIT()
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
                                       
            
            bot.update()


            window.blit(background, (0, 0))
            sprites.draw(window)
            sprites.draw(window)
            if len(foxbot.listaBalas) > 0:
                for x in foxbot.listaBalas:
                    x.insert(window)
                    x.percurso(W,A,S,D)

            pygame.display.update()

        pygame.quit()
        state=QUIT
    
pygame.quit()
