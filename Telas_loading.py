



pygame.mixer.init()

pygame.font.init()
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
font=pygame.font.SysFont(None,235)
texto=font.render('FIGHT BOTS',True,white)
musica_fundo=pygame.mixer.music.load('sound_track.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()


# Defina a área selecionável
area_selecionavel_start = pygame.Rect(360, 470, 270, 100)  # Retângulo (x, y, largura, altura)
area_selecionavel_Instrucao = pygame.Rect(360, 630, 270, 100)  # Retângulo (x, y, largura, altura)


def game_intro(screen):


    inicio = True
    while inicio:

        pygame.display.flip()
        screen.fill(black)
        screen.blit(assets['start_screen'],(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if area_selecionavel_start.collidepoint(mouse_pos):
                        pygame.display.flip()
                        screen.blit(assets['start_screen'], (0,0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    if area_selecionavel_start.collidepoint(mouse_pos):
                        state = PLAYING

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if area_selecionavel_Instrucao.collidepoint(mouse_pos):
                        pygame.display.flip()
                        screen.blit(assets['instructions_screen'],(0,0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    if area_selecionavel_Instrucao.collidepoint(mouse_pos):
                        state = PLAYING


    pygame.display.flip()
    return state
