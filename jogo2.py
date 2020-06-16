'''
Fruits Falling
Autores: Eduardo Heitor Penteado
         Lucas Ohara
         Lucca Montini Argenton
'''
import pygame
import os
import sys
import random
import time 

 

pygame.init()


#------------------------------------------------------
WIDTH = 576
HEIGHT = 576
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruits Falling')
 
FRUIT_WIDTH = 50
FRUIT_HEIGHT = 38
BONECO_WIDTH = 170
BONECO_HEIGHT = 150
BOMB_HEIGHT = 50
BOMB_WIDTH = 50

assets = {}


#----------------Adicionando sons-----------------------
arquivo5 = os.path.join("sound", "Spring Village.ogg")
pygame.mixer.music.load(arquivo5)
arquivo6 = os.path.join('sound', 'pop.wav')
arquivo7 = os.path.join('sound', 'expl3.wav')
pygame.mixer.music.set_volume(0.2)



#-------------------------------------------------------
arquivo0 = os.path.join('img', 'orange.png')
arquivo = os.path.join('img', 'morango.png')
arquivo2 = os.path.join('img', 'dude.png')
arquivo3 = os.path.join('img', 'back4.png')
arquivo4 = os.path.join('img', 'bomb.png')
arquivox = os.path.join('img','init2.png')


#carrega fonte que sera usada no placar
assets["score_font"] = pygame.font.Font('font/PressStart2P.ttf', 28)
 


try: 
    background = pygame.image.load(arquivo3).convert()
    fruit_img = pygame.image.load(arquivo).convert_alpha()
    boneco_img = pygame.image.load(arquivo2).convert_alpha()    
    bomb_img = pygame.image.load(arquivo4).convert_alpha()
    fruit2_img= pygame.image.load(arquivo0).convert_alpha() 
    pop_sound = pygame.mixer.Sound(arquivo6)
    expl_sound = pygame.mixer.Sound(arquivo7)
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
        #reconhece a sprite com seu devido formato
        self.mask = pygame.mask.from_surface(boneco_img)
        

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
        self.mask = pygame.mask.from_surface(fruit_img)
        self.mask = pygame.mask.from_surface(fruit2_img)
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
        self.mask = pygame.mask.from_surface(bomb_img)
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
for i in range(4):
    fruit = Fruit(fruit_img)
    all_sprites.add(fruit)
    all_fruits.add(fruit)
    

for i in range(1):
    fruit2 = Fruit(fruit2_img)
    all_sprites.add(fruit2)
    all_fruits2.add(fruit2)

score = 0
pygame.mixer.music.play(-1)

black=(0,0,0)
end_it=False
while (end_it==False):
    startscreen=pygame.image.load(arquivox)
    window.blit(startscreen, (0,0))
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("Press UP to Start", 1, (255, 255, 255))
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                end_it=True
    window.blit(nlabel,(200,200))
    pygame.display.flip()

# Game Loop
while game:
    if len(all_bombs.sprites()) < (score//150 + 1):
        bomba = Bombs(bomb_img)
        all_sprites.add(bomba)
        all_bombs.add(bomba)
    
    clock.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    hits = pygame.sprite.spritecollide(player, all_bombs, True, pygame.sprite.collide_mask)
    #for all_bombs in hits:  
    for all_bombs in hits:     
        game = False

    hits2 = pygame.sprite.spritecollide(player, all_fruits, True, pygame.sprite.collide_mask)
    hits3 = pygame.sprite.spritecollide(player, all_fruits2, True, pygame.sprite.collide_mask) 
    for fruit in hits2:
        pop_sound.play()
        f = Fruit(fruit_img)
        score += 10               
        all_sprites.add(f)
        all_fruits.add(f)

    for fruit2 in hits3:
        pop_sound.play()
        f2 = Fruit(fruit2_img)
        all_sprites.add(f2)
        all_fruits2.add(f2)
        score += 20

    
    window.fill((0,0,0))
    window.blit(background, [0,0])
    text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    all_sprites.draw(window)
 
    pygame.display.flip()

#finalização
listascore = []
listascore.append(score)
if game == False:
    window.fill((0, 0, 0))
    myfont=pygame.font.SysFont("Britannic Bold", 50)
    nlabel=myfont.render("your score is:{:08d}".format(score), 1, (255, 255, 255))
    nlabel2=myfont.render("Game Over", 1, (255, 0, 0))
    window.blit(nlabel,(100,200))
    window.blit(nlabel2,(200,150))
    pygame.display.flip()
    time.sleep(3)

pygame.quit()


#Referencia 
#Som : patrickdearteaga.com