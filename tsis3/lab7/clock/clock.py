import pygame
from datetime import datetime

pygame.init()


window_size = (829, 836)
screen = pygame.display.set_mode(window_size)


clock_bg = pygame.image.load('clock/images/body.jpeg')
minute_arrow = pygame.image.load('clock/images/right.png')
second_arrow = pygame.image.load('clock/images/left.png')
minute_arrow = pygame.transform.rotate(minute_arrow, 90)
second_arrow = pygame.transform.rotate(second_arrow, 90)


center = (window_size[0] // 2, window_size[1] // 2)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    
    current_time = datetime.now()

  
    minute_angle = 360 - (current_time.minute * 6)
    minute_arrow_rotated = pygame.transform.rotate(minute_arrow, minute_angle)
    minute_pos = ((window_size[0] - minute_arrow_rotated.get_width())/2,(window_size[1] - minute_arrow_rotated.get_height())/2 )

   
    second_angle = 360 - (current_time.second * 6)
    second_arrow_rotated = pygame.transform.rotate(second_arrow, second_angle)
    second_pos = ((window_size[0] - second_arrow_rotated.get_width())/2,(window_size[1] - second_arrow_rotated.get_height())/2 )
   
   
    screen.blit(clock_bg, (0, 0))
    screen.blit(minute_arrow_rotated, minute_pos)
    screen.blit(second_arrow_rotated, second_pos)

   
    pygame.display.update()
    pygame.time.wait(16)
   