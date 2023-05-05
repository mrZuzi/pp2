import pygame, sys, random, time
import psycopg2
from config import params

level = 0


def create_table_snake():
    SQL = (
        '''
        CREATE TABLE IF NOT EXISTS snake ( 
        Name VARCHAR(255) NOT NULL,
        Score int NOT NULL,
        Level int NOT NULL,
        body int NOT NULL,
        head_x int NOT NULL,
        head_y int NOT NULL,
        food_x int NOT NULL,
        food_y int NOT NULL,
        direction varchar(15)
        ) 
        '''
    )

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def create_table_records():
    SQL = (
        '''
        CREATE TABLE IF NOT EXISTS records_snake ( 
        Name VARCHAR(255) NOT NULL,
        Score int NOT NULL
        ) 
        '''
    )

    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def show():
    SQL = "SELECT * FROM records_snake order by score DESC"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        text = " Name                   Score"
        print("\033[36m {}".format(text))
        print("\033[0m", end='')

        for row in res:
            l = len(row[0])
            print(" " + str(row[0]), end="")
            for i in range(24 - l):
                print(' ', end="")
            print(' ', end="")
            print(str(row[1]))


    except Exception as Error:
        print(str(Error))


def add_user(name, score):
    SQL = "INSERT INTO records_snake (Name, Score) VALUES ('" + str(name) + "','" + str(score) + "');"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def update(name, score):
    SQL = "UPDATE records_snake SET score = '" + str(score) + "' WHERE name = '" + str(name) + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))


def check(name, score):
    SQL = "SELECT score FROM records_snake WHERE name = '" + str(name) + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))

    if len(res) == 0:
        add_user(name, score)
    else:
        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        if int(checked) < score:
            update(name, score)
        else:
            print("Your record is:   " + checked)


create_table_records()
create_table_snake()

pygame.init()

FPS = pygame.time.Clock()  # Make game slow
fps = 10
FPS.tick(fps)

a = int(input(
    "What do you want?\n 1-Play                    2-Play paused game                    3 - Look at the table  \n"))
Play = False
if a == 1:
    Play = True
    started = True
    name = input('Write your name: \n')

if a == 3:
    show()
    sys.exit()


def pause(name, score, level, body, head_x, head_y, food_x, food_y, direction):
    SQL = "SELECT * FROM snake where name='" + name + "'"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))

    if len(res) == 0:
        SQL = "INSERT INTO snake (name, score, level, body, head_x, head_y,food_x, food_y, direction) VALUES ('"
        SQL += str(name) + "','" + str(score) + "','" + str(level) + "','" + str(len(body)) + "','" + str(
            head_x) + "','" + str(head_y) + "','" + str(food_x) + "','" + str(food_y) + "','" + direction + "');"
        try:
            config = psycopg2.connect(**params)
            query = config.cursor()
            query.execute(SQL)
            query.close()
            config.commit()

        except Exception as Error:
            print(str(Error))

    else:
        SQL = "UPDATE snake SET score = '" + str(score) + "', level = '" + str(level) + "', body = '" + str(
            len(body)) + "', head_x = '" + str(head_x) + "', head_y = '" + str(head_y) + "', food_x = '" + str(
            food_x) + "', food_y = '" + str(food_y) + "', direction = '" + direction + "' WHERE name = '" + str(
            name) + "';"

        try:
            config = psycopg2.connect(**params)
            query = config.cursor()
            query.execute(SQL)
            query.close()
            config.commit()

        except Exception as Error:
            print(str(Error))


White = (255, 255, 255)
LightSteelBlue = (176, 196, 222)
Red = (255, 0, 0)
Green = (0, 255, 0)  # Colors

height = 500
width = 500
window = (width, height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Lab10 Snake")  # Window settings
step = 20

direction = 'RIGHT'

End = False
append = False

background = pygame.transform.scale(pygame.image.load('snake/images.jpg'), (600, 600))
food = pygame.transform.scale(pygame.image.load("snake/serpent.png"), (20, 20))
font = pygame.font.SysFont('Times New Roman', 24)
score = 0
head_x = head_y = 240
body = [(head_x, head_y), (head_x, head_y), (head_x, head_y)]  # body as array

step = 20
move_x, move_y = 20, 0  # first speed
direction = 'RIGHT'  # first direction
t = 0


def rand():
    return (random.randint(2, 22) * 20)  # random food spawn


food_x = rand()
food_y = rand()

screen.blit(background, (0, 0))
pygame.display.update()

if a == 1:
    time.sleep(5)

# ==============================================================================================================================================================

if a == 2:
    name = input('Write your name: \n')

    SQL = "SELECT score FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        score = int(checked)

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT level FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        level = int(checked)

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT head_x FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        head_x = int(checked)

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT head_y FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        head_y = int(checked)

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT body FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')

        for i in range(int(checked)):
            body.append([head_x, head_y])

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT food_x FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        food_x = int(checked)

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT food_y FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        food_y = int(checked)

    except Exception as Error:
        print(str(Error))

    SQL = "SELECT direction FROM snake where name = '" + name + "';"
    try:
        config = psycopg2.connect(**params)
        query = config.cursor()
        query.execute(SQL)
        res = query.fetchall()
        query.close()
        config.commit()

        checked = str(res[0])
        checked = checked.replace(',', '')
        checked = checked.replace(')', '')
        checked = checked.replace('(', '')
        checked = checked.replace("'", '')
        direction = str(checked)

        if direction == 'DOWN':
            move_x = 0
            move_y = step
        if direction == 'UP':
            move_x = 0
            move_y = -step
        if direction == 'LEFT':
            move_x = -step
            move_y = 0
        if direction == 'RIGHT':
            move_x = step
            move_y = 0


    except Exception as Error:
        print(str(Error))

    Play = True
    started = True
    time.sleep(5)
# ==============================================================================================================================================================
while Play:
    fps = 10 + score / 10
    FPS.tick(fps)
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if pressed[pygame.K_SPACE]:
            pause(name, score, level, body, head_x, head_y, food_x, food_y, direction)
            pygame.quit()
            sys.exit()

        if pressed[pygame.K_DOWN]:
            if direction != 'UP':
                direction = 'DOWN'
                move_x = 0
                move_y = step

        if pressed[pygame.K_UP]:
            if direction != 'DOWN':
                direction = 'UP'
                move_x = 0
                move_y = -step

        if pressed[pygame.K_LEFT]:
            if direction != 'RIGHT':
                direction = 'LEFT'
                move_x = -step
                move_y = 0

        if pressed[pygame.K_RIGHT]:
            if direction != 'LEFT':
                direction = 'RIGHT'
                move_x = step
                move_y = 0  # Head movement directions

    if not End:
        body.append([head_x, head_y])
        body.pop(0)
        if append:
            body.append([head_x, head_y])  # body increase
            score += random.randint(1, 5)
            level += 1
            append = False
        head_x += move_x
        head_y += move_y
        t += 1

        if head_x < 0 or head_x > 480 or head_y < 0 or head_y > 480:  # inside the borders
            End = True

        if t > 100 - level:  # change food location after some amount of movements
            food_x = rand()
            food_y = rand()
            t = 0

        while head_x == food_x and head_y == food_y:
            food_x = rand()
            food_y = rand()
            t = 0
            append = True
        screen.blit(background, (0, 0))
        screen.blit(food, (food_x, food_y))
        pygame.draw.rect(screen, (0, 100, 0), (head_x, head_y, 20, 20))

        for block in body:

            while block[0] == food_x and block[1] == food_y:
                food_x = rand()
                food_y = rand()
                fps = fps + 1
                FPS.tick(fps)

            if head_x == block[0] and head_y == block[1]:
                End = True
                break
            pygame.draw.rect(screen, (0, 200, 0), (block[0], block[1], 20, 20))
            screen.blit(font.render("Score: {}".format(score), True, (255, 0, 0)), (10, 10))
            screen.blit(font.render("Level: {}".format(level), True, (255, 0, 0)), (10, 40))
    else:
        screen.fill((255, 255, 255))
        check(name, score)
        c = False
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (175, 200))  # Game Over
        time.sleep(2)
        sys.exit()

    pygame.display.update()
    if started:
        time.sleep(2)
        started = False