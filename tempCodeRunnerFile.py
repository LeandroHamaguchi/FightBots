    if state == GAMEOVER:
        while state == GAMEOVER:
            text_surface = assets['font'].render('GAME OVER', True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2, HEIGHT / 4)
            screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(2000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE
                if state == GAMEOVER:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            state = DONE
                        if event.key == pygame.K_SPACE:
                            state = PLAYING
                            player.health = 100
                            enemy.health = 30
                            score = 0
                            player.rect.centerx = 100
                            player.rect.centery = HEIGHT / 2
                            enemy.rect.centerx = WIDTH - 100
                            enemy.rect.centery = HEIGHT / 2

    if state == WIN:
        text_surface = assets['font'].render('YOU WIN', True, (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, HEIGHT / 4)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)