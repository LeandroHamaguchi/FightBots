import pygame
pygame.init()
pygame.mixer.init()
pygame.font.init()

#Configurações para a tela do jogo e de jogabilidade
white = (255, 255, 255)
black = (0, 0, 0)
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fight Bots')
clock = pygame.time.Clock()
FPS = 25
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
ENEMY_WIDTH = 200
ENEMY_HEIGHT = 200

#Area selecionável
area_selecionavel_start = pygame.Rect(360, 470, 270, 100)
area_selecionavel_instrucao = pygame.Rect(360, 630, 270, 100)
area_selecionavel_start_hover = pygame.Rect(360, 470, 270, 100)
area_selecionavel_instrucao_hover = pygame.Rect(360, 630, 270, 100)

#Tela de inicio
def game_intro(screen, state):
    introduction = True
    while introduction:
        pygame.display.flip()
        screen.fill(black)
        screen.blit(assets['start_screen'], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                introduction = False

            if event.type == pygame.MOUSEMOTION:
                click = pygame.mouse.get_pos()
                
                if area_selecionavel_start.collidepoint(click):
                    screen.blit(assets['screen_start_select'], (0, 0))
                elif area_selecionavel_instrucao.collidepoint(click):
                    screen.blit(assets['instructions'], (0, 0))
                else:
                    screen.blit(assets['start_screen'], (0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    click = pygame.mouse.get_pos()
                    if area_selecionavel_start.collidepoint(click):
                        state = PLAYING
                        introduction = False
                    elif area_selecionavel_instrucao.collidepoint(click):
                        state = INSTRUCTIONS
                        introduction = False

    return state

#Tela de instruções
def game_instructions(screen, state):
    instructions = True
    while instructions:
        pygame.display.flip()
        screen.fill(black)
        screen.blit(assets['instructions'], (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
                instructions = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = BEGIN
                    instructions = False

    return state

#Imagens, sons e fontes
assets = {}
assets['background'] = pygame.image.load('assets/imgs/background.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
assets['start_screen'] = pygame.image.load('assets/imgs/Tela_Intro.png').convert()
assets['start_screen'] = pygame.transform.scale(assets['start_screen'], (WIDTH, HEIGHT))
assets['instructions'] = pygame.image.load('assets/imgs/tela_instrucoes.jpg').convert()
assets['instructions'] = pygame.transform.scale(assets['instructions'], (WIDTH, HEIGHT))
assets['screen_start_select'] = pygame.image.load('assets/imgs/screen_start_select.png').convert()
assets['screen_start_select'] = pygame.transform.scale(assets['screen_start_select'], (WIDTH, HEIGHT))
assets['player_img'] = pygame.image.load('assets/imgs/player.png').convert_alpha()
assets['player_img'] = pygame.transform.scale(assets['player_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['enemy_img'] = pygame.image.load('assets/imgs/enemy.png').convert_alpha()
assets['enemy_img'] = pygame.transform.scale(assets['enemy_img'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['bullet_img'] = pygame.image.load('assets/imgs/bullet_img.png').convert_alpha()
assets['bullet_img'] = pygame.transform.scale(assets['bullet_img'], (60, 60))
assets['enemy_bullet_img'] = pygame.image.load('assets/imgs/enemy_bullet.png').convert_alpha()
assets['enemy_bullet_img'] = pygame.transform.scale(assets['enemy_bullet_img'], (80, 80))
assets['game_over'] = pygame.image.load('assets/imgs/gameover.png').convert_alpha()
assets['game_over'] = pygame.transform.scale(assets['game_over'], (WIDTH, HEIGHT))
assets['font'] = pygame.font.Font('assets/fonts/valorax-font/Valorax-lg25V.otf', 28)
assets['shoot_sound'] = pygame.mixer.Sound('assets/sounds/shoot.wav')

#Jogador principal
class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['player_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - (WIDTH-100)
        self.rect.bottom = HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.health = 100

        self.shot_timer = pygame.time.get_ticks()
        self.timer_limit = 50

    def update(self):
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT - PLAYER_HEIGHT:
            self.rect.top = HEIGHT - PLAYER_HEIGHT
        if self.rect.bottom < 0 + PLAYER_HEIGHT:
            self.rect.bottom = 0 + PLAYER_HEIGHT            

    def shoot(self):
        assets['shoot_sound'].play()
        new_shot_timer = pygame.time.get_ticks()
        
        if new_shot_timer - self.shot_timer > self.timer_limit:
            self.timer_limit = new_shot_timer
            new_bullet = PlayerBullet(self.assets, self.rect.centery, self.rect.centerx + (PLAYER_WIDTH))
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_player_shots'].add(new_bullet)

#Inimigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['enemy_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 100
        self.rect.bottom = HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.health = 100

        self.shot_timer = pygame.time.get_ticks()
        self.timer_limit = 40

    def update(self):
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT - ENEMY_HEIGHT:
            self.rect.top = HEIGHT - ENEMY_HEIGHT
        if self.rect.bottom < 0 + ENEMY_HEIGHT:
            self.rect.bottom = 0 + ENEMY_HEIGHT

    def shoot(self):
        assets['shoot_sound'].play()
        new_shot_timer = pygame.time.get_ticks()
        
        if new_shot_timer - self.shot_timer > self.timer_limit:
            self.timer_limit = new_shot_timer
            new_bullet = EnemyBullet(self.assets, self.rect.centery, self.rect.centerx - (ENEMY_WIDTH))
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_enemy_shots'].add(new_bullet)

#Bala do jogador
class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx - 200
        self.rect.centery = centery
        self.speedx = 12
        self.assets = assets

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()
        if self.rect.top > HEIGHT:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.collide_mask(self, enemy):
            self.kill()
            enemy.health -= 10

#Bala do inimigo
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['enemy_bullet_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx + 200
        self.rect.centery = centery
        self.shot_speed = 12
        self.speedx = self.shot_speed
        self.speedy = self.shot_speed
        self.assets = assets

    def update(self):
        self.rect.x -= self.speedx

        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()
        if self.rect.top > HEIGHT:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.collide_mask(self, player):
            self.kill()
            player.health -= 10

#Handling sprites
all_sprites = pygame.sprite.Group()
all_enemy_shots = pygame.sprite.Group()
all_player_shots = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_enemy_shots'] = all_enemy_shots
groups['all_player_shots'] = all_player_shots
player = Player(groups, assets)
player_shot = PlayerBullet(assets, player.rect.top, player.rect.centerx)
enemy = Enemy(groups, assets)
enemy_shot = EnemyBullet(assets, enemy.rect.top, enemy.rect.centerx)
all_sprites.add(player)
all_sprites.add(enemy)

#Ajustes da música
soundtrack = pygame.mixer.music.load('assets/sounds/soundtrack.mp3')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(loops=-1)

#Ajustes iniciais do loop principal do jogo
timer = 0
nome = ''
DONE = 0
PLAYING = 1
GAMEOVER = 2
WIN = 3
BEGIN = 4
SKIP = 5
NAME_TO_START=6
INSTRUCTIONS = 7

#Loop principal do jogo
state = NAME_TO_START
while state != DONE:
    screen.fill((0, 0, 0))

    #Tela para digitar nome
    if state == NAME_TO_START:
        text= assets['font'].render( 'Digite seu nome: ' , True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.midtop = (WIDTH / 2, HEIGHT / 4)
        screen.blit(text, text_rect)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        state = DONE
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE: 
                            nome-=event.unicode
                        if event.key == pygame.K_RETURN:
                            state = BEGIN
                        else:
                            nome+=event.unicode

        text_surface = assets['font'].render(nome, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
    
    #Verificando tela de início
    if state == BEGIN:
        state = game_intro(screen, state)

    #Verificando tela de instruções
    if state == INSTRUCTIONS:
        state = game_instructions(screen, state)
    
    #Tela de jogo principal
    if state == PLAYING:
        while state == PLAYING:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE
                if state == PLAYING:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            state = DONE
                        if event.key == pygame.K_w:
                            #bot vai para cima
                            player.speedy = 0
                            player.speedy -= 4
                            enemy.speedy = 0
                            enemy.speedy -= 3
                        if event.key == pygame.K_s:
                            #bot vai para baixo
                            player.speedy = 0
                            player.speedy += 4
                            enemy.speedy = 0
                            enemy.speedy += 3
                        if event.key == pygame.K_SPACE:
                            player.shoot()

            enemy.shoot()
            all_sprites.update()

            if player.health <= 0:
                state = GAMEOVER
            if enemy.health <= 0:
                state = WIN

            screen.fill((0, 0, 0))
            screen.blit(assets['background'], (0, 0))
            all_sprites.draw(screen)

            timer += 1
            score_font_surface = assets['font'].render("{:2d}".format(timer), True, (255, 255, 0))
            text_rect = score_font_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  100)
            screen.blit(score_font_surface, text_rect)

            lives_font_surface = assets['font'].render("{:01d}".format(player.health), True, (255, 255, 0))
            text_rect = lives_font_surface.get_rect()
            text_rect.bottomleft = (80, HEIGHT - 100)
            screen.blit(lives_font_surface, text_rect)

            lives_font_surface = assets['font'].render("{:01d}".format(enemy.health), True, (255, 255, 0))
            text_rect = lives_font_surface.get_rect()
            text_rect.bottomleft = (WIDTH - 120, HEIGHT - 100)
            screen.blit(lives_font_surface, text_rect)

            #Verificando game over
            if state == GAMEOVER:
                while state == GAMEOVER:
                    screen.fill((0, 0, 0))
                    screen.blit(assets['game_over'], (0, 0))
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
            
            #Verificando vitória
            if state == WIN:
                with open('leaderboard.txt', 'a') as tela_tempos:
                        if timer >= 600:
                            tempo = '{0} eliminou o inimigo em {1} minutos'.format(nome,str(timer//60))
                        if timer < 600:           
                            tempo = '{0} eliminou o inimigo em {1} segundos'.format(nome,str(timer//10))
                        tela_tempos.write(tempo)

                text_surface = assets['font'].render('YOU WIN', True, (0, 255, 0))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (WIDTH / 2, HEIGHT / 4)
                screen.blit(text_surface, text_rect)
                
                pygame.display.update()
                pygame.time.wait(5000)

                state = NAME_TO_START

            pygame.display.update()

pygame.quit()