import pygame

pygame.init()

ALTURA = 500
LARGURA = 500
window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption('Fight In Time')
running = True

font = pygame.font.SysFont(None, 48)
texto_intro = font.render('Seja Bem Vindo ao Fight In Time', True, (0, 0, 0))

white = (255, 255, 255)
blue = (0, 255, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    window.fill(white)
    window.blit(texto_intro, (0, 0))
    
    pygame.draw.circle(window, blue, (250, 250), 40)

    pygame.display.update()

pygame.quit()