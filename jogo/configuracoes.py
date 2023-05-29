import pygame

# dimensoes
ALTURA = 750
LARGURA = 1000
#começo e fim da tela inicial
INIT=0
QUIT=1
START=2
# window settings
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Fight Bots')

#Frames por segundo
FPS= 60

# cores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# assets
FOXBOT_LARGURA = 100
FOXBOT_ALTURA = 100

BOT_LARGURA = 100
BOT_ALTURA = 100

BALA_LARGURA = 20
BALA_ALTURA = 40

background = pygame.image.load('assets/background.png').convert()
background = pygame.transform.scale(background,(LARGURA,ALTURA))

Tela_Inicial = pygame.image.load('assets/Tela_Intro.jpg').convert()
Tela_Inicial = pygame.transform.scale(Tela_Inicial,(LARGURA,ALTURA))
Tela_Start = pygame.image.load('assets/Tela_sel_Start.jpg').convert()
Tela_Start = pygame.transform.scale(Tela_Start,(LARGURA,ALTURA))
Tela_Instrucoes = pygame.image.load('assets/Tela_instrucoes.jpg').convert()
Tela_Instrucoes = pygame.transform.scale(Tela_Instrucoes,(LARGURA,ALTURA))


#imagens dos personagens + balas
    #foxbot
foxbot_img = pygame.image.load('assets/foxbot.png').convert_alpha()
foxbot_img = pygame.transform.scale(foxbot_img,(FOXBOT_LARGURA, FOXBOT_ALTURA))
bala_player = pygame.image.load('assets/Bullet_player.png').convert_alpha()
bala_player = pygame.transform.scale(bala_player,(BALA_LARGURA,BALA_ALTURA))

    #bot
bot_img= pygame.image.load('assets/bot.jpg').convert_alpha()
bot_img = pygame.transform.scale(bot_img,(BOT_LARGURA, BOT_ALTURA))
bala_bot= pygame.image.load('assets/Bullet_enemy.png').convert_alpha()
bala_bot= pygame.transform.scale(bala_bot,(BALA_LARGURA,BALA_ALTURA))


# listas que guardam as balas
listaBalas_Inimigo=[]
listaBalas=[]

# posição inicial do player
W_inicial=0
S_inicial=0
D_inicial=1
A_inicial=0