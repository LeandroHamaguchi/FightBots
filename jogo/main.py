import pygame
import sys
sys.path.append('personagens')
from foxbot import Foxbot
from bot import Bot

pygame.init()
pygame.mixer.init()

# dimensoes
ALTURA = 500
LARGURA = 500

# cores
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# window settings
window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('Fight Bots')
background = pygame.image.load('background')

# fontes
font = pygame.font.SysFont(None, 48)
texto_intro = font.render('Seja Bem Vindo a Fight Bots!', True, (0, 0, 0))

# propriedades dos personagens
fox_x = 10
fox_y = 250
fox1_width = 10
fox1_height = 10
fox2_width = 10
fox2_height = 10

bot_x = 450
bot_y = 250
bot1_width = 10
bot1_height = 10
bot2_width = 10
bot2_height = 10

# personagens e classes
foxbot1 = Foxbot(fox_draw)
bot1 = Bot(bot_draw)
foxbot2 = Foxbot(fox_draw)
bot2 = Bot(bot_draw)

foxbot1.draw.rect(window, red, (fox_x, fox_y, fox1_width, fox1_height))
bot1.draw.rect(window, blue, (bot_x, bot_y, bot1_width, bot1_height))
foxbot2.draw.rect(window,blue, (fox_x, fox_y, fox2_width, fox2_height))
bot2.draw.rect(window,red, (bot_x, bot_y, bot2_width, bot2_height))



# plot
DONE = False
PLAYING = True
state = PLAYING
clock = pygame.time.Clock()
FPS = 30

# main loop do jogo
while state != DONE:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = DONE
        elif state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = DONE
                if event.key == pygame.K_UP:
                    new_speedx = 0
                    new_speedy = 10
                    foxbot.update(new_speedx, new_speedy)
                if event.key == pygame.K_LEFT:
                    new_speedx = -10
                    new_speedy = 0
                    foxbot.update(new_speedx, new_speedy)
                if event.key == pygame.K_DOWN:
                    new_speedx = 0
                    new_speedy = -10
                    foxbot.update(new_speedx, new_speedy)
                if event.key == pygame.K_RIGHT:
                    new_speedx = 10
                    new_speedy = 0
                    foxbot.update(new_speedx, new_speedy)

    bot.update()

    window.fill(white)

    

    pygame.display.update()

pygame.quit()