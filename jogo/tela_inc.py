import pygame
import sys
from main import *

pygame.font.init()
pygame.font.quit()

Black=(0,0,0)

def text_objects(texto, fonte):
    introducao = fonte.render(texto, True, Black)
    return introducao, introducao.get_rect()

def game_intro():

    inicio = True

    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        window.fill(Black)
        largeText = pygame.font.Font('arial',24)
        introducao = text_objects("Fight Bots", largeText)
        introducao.center = (((0)),(LARGURA/2))
        window.blit(introducao)
        pygame.display.update()
        clock.tick(15)