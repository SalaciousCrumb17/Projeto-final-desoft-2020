import pygame
import os
import sys
import random

pygame.init()

#------------------------------------------------------
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruits Falling')

FRUIT_WIDTH = 50
FRUIT_HEIGHT = 38
BONECO_WIDTH = 125
BONECO_HEIGHT = 100
BOMB_HEIGHT = 50
BOMB_WIDTH = 50
#-------------------------------------------------------
arquivo0 = os.path.join('img', 'orange.png')
arquivo = os.path.join('img', 'morango.png')
arquivo2 = os.path.join('img', 'boneco1.png')
arquivo3 = os.path.join('img', 'back4.png')
arquivo4 = os.path.join('img', 'bomb.png')

try:
    background = pygame.image.load(arquivo3).convert()
    fruit_img = pygame.image.load(arquivo).convert_alpha()
    boneco_img = pygame.image.load(arquivo2).convert_alpha()    
    bomb_img = pygame.image.load(arquivo4).convert_alpha()
    fruit2_img= pygame.image.load(arquivo0).convert_alpha()
except pygame.error:
    sys.exit()
fruit_img = pygame.transform.scale(fruit_img, (FRUIT_WIDTH, FRUIT_HEIGHT))
fruit2_img = pygame.transform.scale(fruit2_img, (FRUIT_WIDTH, FRUIT_HEIGHT))
boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, BONECO_HEIGHT))
bomb_img = pygame.transform.scale(bomb_img, (BOMB_WIDTH, BOMB_HEIGHT))
#-------------------------------------------------------
class Boneco(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Fruit(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-FRUIT_WIDTH)
        self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
        self.speedy = random.randint(2, 5)
        
    def update(self):
        # Atualizando a posição da fruta 
        self.rect.y += self.speedy
        # Se a fruta passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-FRUIT_WIDTH)
            self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
            self.speedy = random.randint(2, 5)

class Bombs(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-FRUIT_WIDTH)
        self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
        self.speedy = random.randint(2, 5)
        
    def update(self):
        # Atualizando a posição da bomba  
        self.rect.y += self.speedy
        # Se a bomba passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-FRUIT_WIDTH)
            self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
            self.speedy = random.randint(2, 5)


# Limita fps
clock = pygame.time.Clock()
FPS = 60

game = True


#criando grupo 
all_sprites = pygame.sprite.Group()
all_fruits = pygame.sprite.Group()
all_fruits2 = pygame.sprite.Group()
all_bombs = pygame.sprite.Group()
#criando player
player = Boneco(boneco_img)
all_sprites.add(player)
#cria frutas
for i in range(1):
    fruit = Fruit(fruit_img)
    all_sprites.add(fruit)
    all_fruits.add(fruit)
    

for i in range(1):
    fruit2 = Fruit(fruit2_img)
    all_sprites.add(fruit2)
    all_fruits.add(fruit2)

    
for i in range(1):
    bomba = Bombs(bomb_img)
    all_sprites.add(bomba)
    all_bombs.add(bomba)

# Game Loop
while game:
    clock.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit
            game = False
        if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8

    all_sprites.update()

      # Verifica se houve contato entre o player e a bomba
    hits = pygame.sprite.spritecollide(player, all_bombs, True)
    if len(hits) > 0:
       game = False

    hits2 = pygame.sprite.spritecollide(player, all_fruits, True)
    hits3 = pygame.sprite.spritecollide(player, all_fruits2, True) 
    for fruit in hits2:
        f = Fruit(fruit_img)
        
        
        all_sprites.add(f)
        all_fruits.add(f)
    for fruit2 in hits3:
        f2 = Fruit(fruit2_img)

        all_sprites.add(f2)
        all_fruits.add(f2)



 
    window.fill((0,0,0))
    window.blit(background, [0,0])
    
    all_sprites.draw(window)

    pygame.display.flip()

#finalização
pygame.quit()

#DUVIDAS: Para colocar as bombas e os power ups, é necessario criar uma classe para cada um deles?
#         Como vamos fazer para que quando o player toque na fruta ela desapareça?
#         Vamos colocar 2 players? Como? Mais uma classe e tela dividida ou a mesma tela?