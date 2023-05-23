import pygame

import sys
pygame.mixer.init()
from configuracoes import window,START,QUIT
pygame.font.init()
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,235)
texto=font.render('FIGHT BOTS',True,white)
musica_fundo=pygame.mixer.music.load('assets/sons/stomping-rock-four-shots-111444.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
def game_intro(screen):


    inicio = True
    while inicio:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                inicio = False

            if event.type == pygame.KEYUP:
                state = START
                inicio = False
                
        window.fill(black)
        window.blit(texto,(0,10))

        
        pygame.display.flip()

    return state