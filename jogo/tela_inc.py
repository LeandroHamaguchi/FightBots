import pygame
import sys
from configuracoes import window,START,QUIT
pygame.font.init()
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,248)
texto=font.render('FIGHT BOTS',True,white)

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
        window.blit(texto,(100,10))
        
        pygame.display.flip()

    return state