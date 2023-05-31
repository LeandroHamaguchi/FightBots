import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fight in Time')

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
assets = {}
assets['background'] = pygame.image.load('background.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
assets['player_img'] = pygame.image.load('player_teste.png').convert_alpha()
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

#assets['explosion_sound'] = pygame.mixer.Sound('assets/snd/explosion.wav')
#assets['shoot_sound'] = pygame.mixer.Sound('assets/snd/shoot.wav')
#assets['enemy_shoot_sound'] = pygame.mixer.Sound('assets/snd/enemy_shoot.wav')
#assets['music'] = pygame.mixer.music.load('assets/snd/music.mp3')

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

        self.shot_timer = pygame.time.get_ticks()
        self.timer_limit = 50

    def update(self):
        self.rect.x += self.speedx
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
        #assets['shoot_sound'].play()
        new_shot_timer = pygame.time.get_ticks()
        
        if new_shot_timer - self.shot_timer > self.timer_limit:
            self.timer_limit = new_shot_timer
            new_bullet = PlayerBullet(self.assets, self.rect.centery, self.rect.centerx + (PLAYER_WIDTH))
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_player_shots'].add(new_bullet)

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

        self.shot_timer = pygame.time.get_ticks()
        self.timer_limit = 40

    def update(self):
        self.rect.x += self.speedx
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
        #assets['shoot_sound'].play()
        new_shot_timer = pygame.time.get_ticks()
        
        if new_shot_timer - self.shot_timer > self.timer_limit:
            self.timer_limit = new_shot_timer
            new_bullet = EnemyBullet(self.assets, self.rect.centery, self.rect.centerx - (ENEMY_WIDTH))
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_enemy_shots'].add(new_bullet)

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
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
            #assets['explosion_sound'].play()
            #explosion = Explosion(enemy.rect.center, assets)
            #all_sprites.add(explosion)
            #state = EXPLODING
            #explosion_group.add(explosion)
            #enemy = Enemy(groups, assets)
            #all_sprites.add(enemy)
            #enemy_group.add(enemy)
            #score += 100

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, assets, centery, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['enemy_bullet_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.shot_speed = 12
        self.speedx = self.shot_speed
        self.speedy = self.shot_speed
        self.assets = assets

    def update(self):
        if player.speedx > 0:
            if player.speedy > 0:
                self.speedx = self.shot_speed
                self.speedy = -self.shot_speed
            elif player.speedy < 0:
                self.speedx = self.shot_speed
                self.speedy = self.shot_speed
            else:
                self.speedx = self.shot_speed
                self.speedy = 0
        elif player.speedx < 0:
            if player.speedy > 0:
                self.speedx = -self.shot_speed
                self.speedy = -self.shot_speed
            elif player.speedy < 0:
                self.speedx = -self.shot_speed
                self.speedy = self.shot_speed
            else:
                self.speedx = -self.shot_speed
                self.speedy = 0
        else:
            if player.speedy > 0:
                self.speedx = 0
                self.speedy = -self.shot_speed
            elif player.speedy < 0:
                self.speedx = 0
                self.speedy = self.shot_speed
            else:
                self.speedx = 0
                self.speedy = 0

        self.rect.x += self.speedx
        self.rect.y += self.speedy

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
            #assets['explosion_sound'].play()
            #explosion = Explosion(enemy.rect.center, assets)
            #all_sprites.add(explosion)
            #state = EXPLODING
            #explosion_group.add(explosion)
            #enemy = Enemy(groups, assets)
            #all_sprites.add(enemy)
            #enemy_group.add(enemy)
            #score += 100

#pygame.mixer.music.set_volume(0.4)
#pygame.mixer.music.play(loops=-1)
clock = pygame.time.Clock()
FPS = 30

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

DONE = 0
PLAYING = 1
GAMEOVER = 2
state = PLAYING

score = 0
player_lives = 100
enemy_lives = 100

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
                    player.speedy -= 4
                    enemy.speedy -= 3
                    assets['player_img_w'] = 0
                    if player.image == assets['player_img_w']:
                        pass
                    else:
                        assets['player_img_w'] = pygame.transform.rotate(player.image, 90)
                        player.image = assets['player_img_w']
                if event.key == pygame.K_s:
                    #bot vai para baixo
                    player.speedy += 4
                    enemy.speedy += 3
                    assets['player_img_s'] = 0
                    if player.image == assets['player_img_s']:
                        pass
                    else:
                        assets['player_img_s'] = pygame.transform.rotate(player.image, -90)
                        player.image = assets['player_img_s']
                if event.key == pygame.K_a:
                    #bot vai para esquerda
                    player.speedx -= 4
                    enemy.speedx -= 3
                    assets['player_img_a'] = 0
                    if player.image == assets['player_img_a']:
                        pass
                    else:
                        assets['player_img_a'] = pygame.transform.rotate(player.image, 180)
                        player.image = assets['player_img_a']
                if event.key == pygame.K_d:
                    #bot vai para direita
                    player.speedx += 4
                    enemy.speedx += 3
                    assets['player_img'] = pygame.transform.rotate(player.image, 0)
                    player.image = assets['player_img']
                if event.key == pygame.K_SPACE:
                    if player.speedx == 0 and player.speedy < 0:
                        player.shoot()
                    elif player.speedx == 0 and player.speedy > 0:
                        player.shoot()
                    elif player.speedx < 0 and player.speedy == 0:
                        player.shoot()
                    elif player.speedx > 0 and player.speedy == 0:
                        player.shoot()

    enemy.shoot()
    all_sprites.update()

    enemy_hit_box = pygame.sprite.spritecollide(enemy, all_player_shots, True)
    if len(enemy_hit_box) > 0:
        for hit in enemy_hit_box:
            all_sprites.remove(hit)
            all_player_shots.remove(hit)
            enemy_lives -= 10

    player_hit_box = pygame.sprite.spritecollide(player, all_enemy_shots, True)
    if len(player_hit_box) > 0:
        for hit in player_hit_box:
            all_sprites.remove(hit)
            all_enemy_shots.remove(hit)
            player_lives -= 10

    screen.fill((0, 0, 0))
    screen.blit(assets['background'], (0, 0))

    all_sprites.draw(screen)

    score += 1
    score_font_surface = assets['font'].render("{:010d}".format(score), True, (255, 255, 0))
    text_rect = score_font_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    screen.blit(score_font_surface, text_rect)

    lives_font_surface = assets['font'].render("{:01d}".format(player_lives), True, (255, 255, 0))
    text_rect = lives_font_surface.get_rect()
    text_rect.bottomleft = (10, HEIGHT - 10)
    screen.blit(lives_font_surface, text_rect)

    lives_font_surface = assets['font'].render("{:01d}".format(enemy_lives), True, (255, 255, 0))
    text_rect = lives_font_surface.get_rect()
    text_rect.bottomleft = (WIDTH - 80, HEIGHT - 10)
    screen.blit(lives_font_surface, text_rect)
    
    pygame.display.update()