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

# cores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# assets
FOXBOT_LARGURA = 100
FOXBOT_ALTURA = 100

BOT_LARGURA = 90
BOT_ALTURA = 90

BALA_LARGURA = 20
BALA_ALTURA = 40

background = pygame.image.load('assets/background.png').convert()
background = pygame.transform.scale(background,(LARGURA,ALTURA))
foxbot_img = pygame.image.load('assets/foxbot_K_D.png').convert_alpha()
foxbot_img = pygame.transform.scale(foxbot_img,(FOXBOT_LARGURA, FOXBOT_ALTURA))

Tela_Inicial = pygame.image.load('assets/Tela_Intro.jpg').convert()
Tela_Inicial = pygame.transform.scale(Tela_Inicial,(LARGURA,ALTURA))
Tela_Start = pygame.image.load('assets/Tela_sel_Start.jpg').convert()
Tela_Start = pygame.transform.scale(Tela_Start,(LARGURA,ALTURA))
Tela_Instrucoes = pygame.image.load('assets/Tela_instrucoes.jpg').convert()
Tela_Instrucoes = pygame.transform.scale(Tela_Instrucoes,(LARGURA,ALTURA))



bot_img_0 = pygame.image.load('assets/bot_K_A.png').convert_alpha()
bot_img_0 = pygame.transform.scale(bot_img_0,(BOT_LARGURA, BOT_ALTURA))
bot_img_W = pygame.image.load('assets/bot_K_A.png').convert_alpha()
bot_img_W = pygame.transform.scale(bot_img_W,(BOT_LARGURA, BOT_ALTURA))
bot_img_S = pygame.image.load('assets/bot_K_A.png').convert_alpha()
bot_img_S = pygame.transform.scale(bot_img_S,(BOT_LARGURA, BOT_ALTURA))
bot_img_D = pygame.image.load('assets/bot_K_A.png').convert_alpha()
bot_img_D = pygame.transform.scale(bot_img_D,(BOT_LARGURA, BOT_ALTURA))
bala_player= pygame.image.load('assets/Bullet_player.png').convert_alpha()
bala_player= pygame.transform.scale(bala_player,(BALA_LARGURA,BALA_ALTURA))
bala_bot= pygame.image.load('assets/Bullet_enemy.png').convert_alpha()
bala_bot= pygame.transform.scale(bala_bot,(BALA_LARGURA,BALA_ALTURA))