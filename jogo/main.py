import pygame
import foxbot as foxbot
import bot as bot
from tela_inc import game_intro
from configuracoes import *
pygame.init()

<<<<<<< HEAD
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
=======
# dimensoes
ALTURA = 500
LARGURA = 500

# cores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# assets
FOXBOT_LARGURA = 20
FOXBOT_ALTURA = 20
BOT_LARGURA = 20
BOT_ALTURA = 20
background = pygame.image.load('../assets/background.png').convert()
foxbot_img_0 = pygame.image.load('../assets/foxbot_K_D.png').convert_alpha()
foxbot_img_0 = pygame.transform.scale(foxbot_img_0,(FOXBOT_LARGURA, FOXBOT_ALTURA))
foxbot_img_W = pygame.image.load('../assets/foxbot_K_D.png').convert_alpha()
foxbot_img_W = pygame.transform.scale(foxbot_img_W,(FOXBOT_LARGURA, FOXBOT_ALTURA))
foxbot_img_A = pygame.image.load('../assets/foxbot_K_D.png').convert_alpha()
foxbot_img_A = pygame.transform.scale(foxbot_img_A,(FOXBOT_LARGURA, FOXBOT_ALTURA))
foxbot_img_S = pygame.image.load('../assets/foxbot_K_D.png').convert_alpha()
foxbot_img_S = pygame.transform.scale(foxbot_img_S,(FOXBOT_LARGURA, FOXBOT_ALTURA))
bot_img_0 = pygame.image.load('../assets/bot_K_A.png').convert_alpha()
bot_img_0 = pygame.transform.scale(bot_img_0,(BOT_LARGURA, BOT_ALTURA))
bot_img_W = pygame.image.load('../assets/bot_K_A.png').convert_alpha()
bot_img_W = pygame.transform.scale(bot_img_W,(BOT_LARGURA, BOT_ALTURA))
bot_img_S = pygame.image.load('../assets/bot_K_A.png').convert_alpha()
bot_img_S = pygame.transform.scale(bot_img_S,(BOT_LARGURA, BOT_ALTURA))
bot_img_D = pygame.image.load('../assets/bot_K_A.png').convert_alpha()
bot_img_D = pygame.transform.scale(bot_img_D,(BOT_LARGURA, BOT_ALTURA))

# window settings
window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('Fight Bots')
background = pygame.image.load('../assets/background.png')

# personagens e classes

foxbot = Foxbot(foxbot_img_0)
bot = Bot(bot_img_0)

running = True

while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                foxbot.speedy += 10
                Foxbot(foxbot_img_W)
            if event.type == pygame.K_DOWN:
                foxbot.speedy -= 10
                Foxbot(foxbot_img_S)
            if event.type == pygame.K_RIGHT:
                foxbot.speedx += 10
                Foxbot(foxbot_img_0)
            if event.type == pygame.K_LEFT:
                foxbot.speedx -= 10
                Foxbot(foxbot_img_A)
    
    bot.update()

    window.fill(white)
    window.blit(background, (0, 0))

    foxbot.draw(window)
    bot.draw(window)
>>>>>>> joao

        pygame.quit()
        state=QUIT
