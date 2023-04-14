#Imports and initializing
import random
import time
import pygame
pygame.init()
fps = pygame.time.Clock()
#Display settings
W, H = 800, 800
SIZE = 40
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")

#Tick Rate
clock = pygame.time.Clock()
FPS = 6

#Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Font
font_big = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font_big.render("Game Over", True, RED) 

#Other Varaibles
SCORE = 0
SPEED = 5
level_score = 0
total_score = 0
LEVEL = 0
dx, dy = 0, 0
locked_keys = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}

#Grid Draw function
def grid():
    for x in range(0, W, SIZE):
        for y in range(0, H, SIZE):
            rect = pygame.Rect(x, y, SIZE, SIZE)
            pygame.draw.rect(sc, (50, 50, 50), rect, 1)

#Class Point to strore two variables like one
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
#Class Wall takes notes from txt file and builts walls in game screen
class Wall:
    def __init__(self, LEVEL):
        self.wall = []
        self.LEVEL = LEVEL
        f = open("level{}.txt".format(self.LEVEL), "r")
#appending wall point to list
        for y in range(0, H // SIZE + 1):
            for x in range(0, W // SIZE + 1):
                if f.read(1) == '#':
                    self.wall.append(Point(x, y))
#draw function draws walls on the screen
    def draw(self):
        for point in range(0, len(self.wall) - 1):
            rect = pygame.Rect(self.wall[point].x * SIZE, self.wall[point].y * SIZE, SIZE, SIZE)
            pygame.draw.rect(sc, BLUE, rect)

#Class Food where function generate generates food randomly and draw function draws food on the plane
class Food:
    def __init__(self):
        self.location = []
#generate_food function generates food randomly
    def generate_food(self, S1, L1):
        running = True
        while running:
            running = False
            self.location = Point(random.randint(0, W / SIZE - 1), random.randint(0, H / SIZE - 1))
            for i in range(len(S1.snake)):
                if self.location.x == S1.snake[i].x and self.location.y == S1.snake[i].y:
                    running = True
            for i in range(len(L1.wall)):
                if self.location.x == L1.wall[i].x and self.location.y == L1.wall[i].y:
                    running = True
#draw function draws food on the screen
    def draw(self):
        rect = pygame.Rect(self.location.x * SIZE, self.location.y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, RED, rect)
    
#Snake class
class Snake:
    def __init__(self):
        self.x = 10
        self.y = 11
        self.snake =[Point(self.x, self.y)]
#move function: moves the snake in the for loop, iterates the snake from tail to head, each segment takes positions in front of them
    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].x = self.snake[i - 1].x
            self.snake[i].y = self.snake[i - 1].y
        
        self.snake[0].x += dx
        self.snake[0].y += dy
        
        if self.snake[0].x * SIZE> W: self.snake[0].x = 0
        if self.snake[0].x * SIZE< 0: self.snake[0].x = W / SIZE
        if self.snake[0].y * SIZE> H: self.snake[0].y = 0
        if self.snake[0].y * SIZE< 0: self.snake[0].y = H / SIZE
#draw function draws a snake on the screen
    def draw(self):
        point = self.snake[0]
        rect = pygame.Rect(point.x * SIZE, point.y * SIZE, SIZE, SIZE)
        pygame.draw.rect(sc, WHITE, rect)
        for point in self.snake[1:]:
            rect = pygame.Rect(point.x * SIZE, point.y * SIZE, SIZE, SIZE)
            pygame.draw.rect(sc, GREEN, rect)

#check_collision function: check the position of the snake's head relative to the food, the wall and its body. 
#If the snakehead collides with food, its length will increase by 1 point, otherwise the game will be over
    def check_collision(self, S1, F1, L1):
        global total_score
        global SCORE
#Checks if the snake's head has collided with food
        if self.snake[0].x == F1.location.x and self.snake[0].y == F1.location.y:
            self.snake.append(Point(F1.location.x, F1.location.y))
            SCORE += 1
            total_score += 1
            F1.generate_food(S1, L1)
#Checs if the snake's head has collided with its body
        for i in range(1, len(self.snake) - 1):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                sc.blit(game_over, (220, 240))
                sc.blit(score, (340, 360))
                pygame.display.update()
                time.sleep(2)
                pygame.quit()
#Checs if the snake's head has collided with wall
        for i in range(0 ,len(L1.wall) - 1):
            if self.snake[0].x == L1.wall[i].x and self.snake[0].y == L1.wall[i].y:
                sc.blit(game_over, (220, 240))
                sc.blit(score, (340, 360))
                pygame.display.update()
                time.sleep(2)
                pygame.quit()

S1 = Snake()
L1 = Wall(LEVEL)
F1 = Food()
F1.generate_food(S1, L1)

#Main Loop
flag = False
flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.KEYDOWN: #Accepts pressed keys from the user and works with them, also blocks the opposite type of movement
            if event.key == pygame.K_UP and locked_keys['UP']:
                locked_keys = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
                dy = -1
                dx = 0
            elif event.key == pygame.K_DOWN and locked_keys['DOWN']:
                locked_keys = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
                dy = 1
                dx = 0
            elif event.key == pygame.K_LEFT and locked_keys['LEFT']:
                locked_keys = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
                dy = 0
                dx = -1
            elif event.key == pygame.K_RIGHT and locked_keys['RIGHT']:
                locked_keys = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}
                dy = 0
                dx = 1
#Next level
    if SCORE > 4:
        level_score += 1
        LEVEL += 1
        FPS += 1
        if LEVEL == 4:
            LEVEL = 0
        SCORE = 0
        sc.fill(BLACK)
        L1.draw()
        S1.draw()
        L1 = Wall(LEVEL)
        S1 = Snake()
        F1.generate_food(S1, L1)
        grid()
        pygame.display.update()
        flag = True
#Working with display
    sc.fill(BLACK)
    score = font_small.render(f'SCORE: {total_score}', True, WHITE)
    level = font_small.render(f'LEVEL: {level_score + 1}', True, WHITE)
    S1.check_collision(S1, F1, L1)

    S1.move()
    F1.draw()
    S1.draw()
    L1.draw()
    grid()
    sc.blit(score, (10, 10))
    sc.blit(level, (700, 10))
    pygame.display.update()
    clock.tick(FPS)
    if flag:
        flag = False
        time.sleep(1)
pygame.quit()
fps(60)