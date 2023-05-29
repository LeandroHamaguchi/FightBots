import pygame
from configuracoes import Tela_Inicial,Tela_Start,Tela_Instrucoes
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


# Defina a área selecionável
area_selecionavel_start = pygame.Rect(360, 470, 270, 100)  # Retângulo (x, y, largura, altura)
area_selecionavel_Instrucao = pygame.Rect(360, 630, 270, 100)  # Retângulo (x, y, largura, altura)


def game_intro(screen):


    inicio = True
    while inicio:

        pygame.display.flip()
        window.fill(black)
        window.blit(Tela_Inicial,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                inicio = False

            if event.type == pygame.KEYUP:
                state = START
                inicio = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if area_selecionavel_start.collidepoint(mouse_pos):
                        pygame.display.flip()
                        window.blit(Tela_Start,(0,0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    if area_selecionavel_start.collidepoint(mouse_pos):
                        state = START
                        inicio = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if area_selecionavel_Instrucao.collidepoint(mouse_pos):
                        pygame.display.flip()
                        window.blit(Tela_Instrucoes,(0,0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    if area_selecionavel_Instrucao.collidepoint(mouse_pos):
                        state = START
                        inicio = False

    pygame.display.flip()
    return state

