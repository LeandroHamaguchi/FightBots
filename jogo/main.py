import pygame
import foxbot as foxbot
import bot as bot
from tela_inc import game_intro
from configuracoes import *
pygame.init()
pygame.mixer.init()

# personagens e classes
foxbot = foxbot.Foxbot(foxbot_img_0)
bot = bot.Bot(bot_img_0)
sprites = pygame.sprite.Group()
sprites.add(foxbot)
sprites.add(bot)

# loop principal do jogo
running=True
state= INIT
while state != QUIT:
    if state==INIT:
        state=  game_intro(window)
    elif state==START:
        while running:
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
                            foxbot.update()
                            #Foxbot(foxbot_img_W)
                        if event.key == pygame.K_s:
                            foxbot.speedy = 0
                            foxbot.speedy += 15
                            foxbot.speedx = 0
                            foxbot.update()
                            #Foxbot(foxbot_img_S)
                        if event.key == pygame.K_a:
                            foxbot.speedx = 0
                            foxbot.speedx -= 15
                            foxbot.speedy = 0
                            foxbot.update()
                            #Foxbot(foxbot_img_0)
                        if event.key == pygame.K_d:
                            foxbot.speedx = 0
                            foxbot.speedx += 15
                            foxbot.speedy = 0
                            foxbot.update()
                            #Foxbot(foxbot_img_A)
            
            bot.update()


            window.blit(background, (0, 0))

            sprites.draw(window)
            sprites.draw(window)

            pygame.display.update()

        pygame.quit()
        state=QUIT
