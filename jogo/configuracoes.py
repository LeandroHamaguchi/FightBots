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
foxbot_img_0 = pygame.image.load('assets/foxbot_K_D.png').convert_alpha()
foxbot_img_0 = pygame.transform.scale(foxbot_img_0,(FOXBOT_LARGURA, FOXBOT_ALTURA))
foxbot_img_W = pygame.image.load('assets/foxbot_K_D.png').convert_alpha()
foxbot_img_W = pygame.transform.scale(foxbot_img_W,(FOXBOT_LARGURA, FOXBOT_ALTURA))
foxbot_img_A = pygame.image.load('assets/foxbot_K_D.png').convert_alpha()
foxbot_img_A = pygame.transform.scale(foxbot_img_A,(FOXBOT_LARGURA, FOXBOT_ALTURA))
foxbot_img_S = pygame.image.load('assets/foxbot_K_D.png').convert_alpha()
foxbot_img_S = pygame.transform.scale(foxbot_img_S,(FOXBOT_LARGURA, FOXBOT_ALTURA))
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
Fox_imgs=[foxbot_img_W,foxbot_img_S,foxbot_img_A,foxbot_img_0]