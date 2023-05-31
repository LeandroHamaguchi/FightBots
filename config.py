

assets = {}
assets['background'] = pygame.image.load('background.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
assets['start_screen'] = pygame.image.load('Tela_Intro.png').convert()
assets['start_screen'] = pygame.transform.scale(assets['start_screen'], (WIDTH, HEIGHT))
assets['instructions_screen'] = pygame.image.load('instructions_scren.png').convert()
assets['instructions_screen'] = pygame.transform.scale(assets['instructions_screen'], (WIDTH, HEIGHT))

assets['player_img'] = pygame.image.load('player.png').convert_alpha()
assets['player_img'] = pygame.transform.scale(assets['player_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['enemy_img'] = pygame.image.load('enemy.png').convert_alpha()
assets['enemy_img'] = pygame.transform.scale(assets['enemy_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['bullet_img'] = pygame.image.load('bullet_img.png').convert_alpha()
assets['bullet_img'] = pygame.transform.scale(assets['bullet_img'], (20, 20))
assets['enemy_bullet_img'] = pygame.image.load('enemy_bullet.png').convert_alpha()
assets['enemy_bullet_img'] = pygame.transform.scale(assets['enemy_bullet_img'], (20, 20))
#assets['explosion_img'] = pygame.image.load('explosion.png').convert_alpha()
#assets['explosion_img'] = pygame.transform.scale(assets['explosion_img'], (100, 100))
assets['font'] = pygame.font.Font('valorax-font/Valorax-lg25V.otf', 28)