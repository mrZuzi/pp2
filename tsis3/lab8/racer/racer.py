import pygame
from pygame.locals import *
import random, time



FPS = pygame.time.Clock()
pygame.init()
window_size = (400,600)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
# Create a white screen
screen = pygame.display.set_mode((window_size[0],window_size[1]))


font = pygame.font.Font('Fonts/Roboto-Bold.ttf',48)
font_small = pygame.font.Font('Fonts/Roboto-Bold.ttf',20)
game_over = font.render("Game Over", True, 'BLACK')
bg = pygame.image.load("image/AnimatedStreet.png").convert_alpha()
pygame.display.set_caption("The Fast and the Furious")
coin = pygame.image.load("image/coin (1).png"),
coini = 0
coins = 0 
coinscore = 0 
speed = 5
score = 0
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("image/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            score+=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("image/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)    
        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = coin[coini]
        self.image.set_colorkey("WHITE") 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(32, SCREEN_WIDTH - 32), -31)
        self.a = random.randint(400, 600)

    def move(self):
        global coinscore
        self.rect.move_ip(0, 2)
        if self.rect.top > 600:
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH - 32), -31)
        elif self.rect.colliderect(P1):
            coinscore += random.randint(1,5)
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH - 32), -31)         
 
 
enemies = []
         
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemiesSprite = pygame.sprite.Group()
enemiesSprite.add(E1)
enemies.append(E1)

# Creating Sprites Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
Coins = pygame.sprite.Group()
Coins.add(C1)

INC_speed = pygame.USEREVENT + 1
pygame.time.set_timer(INC_speed,1000)
bgy = 0
coin_y = - 62
coin_x = 0
y = 0
bgsound = pygame.mixer.Sound("sound/background.wav")
bgsound.play()

# Game Loop
while True:
    screen.blit(bg , (0,0))   
    
    
    for event in pygame.event.get():
        if event.type == INC_speed:
              speed += 0.25
           
        if event.type == QUIT:
            pygame.quit() 
    if coini == 23:
        coini = 0
    else:
        coini += 1
    if bgy < 600:
        bgy += 7
    else:
        bgy = 0          
    coinscores = font_small.render(str(coinscore), True, "BLACK")
    scores = font_small.render(str(score), True, "BLACK")
    screen.blit(coinscores, (360, 10))
    screen.blit(scores, (10,10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    P1.move()
    
    for enemy in enemies:
        enemy.move()
    for el in Coins:
        screen.blit(el.image, el.rect)
        el.move()    

    if pygame.sprite.spritecollideany(P1, enemies):
          screen.fill('red')
          pygame.mixer.Sound('sound/crash.wav').play()
          time.sleep(0.5)
          screen.blit(game_over, (90,250))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
              
         
    pygame.display.update()
    FPS.tick(60)
    