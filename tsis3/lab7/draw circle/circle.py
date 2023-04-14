import pygame

pygame.init()
window_size = (400,400)
screen = pygame.display.set_mode(window_size)
ball_pos = [window_size[0] // 2, window_size[1] // 2]
ball_radius = 25
movement_amount = 20

while True:
    bg = screen.fill((255,255,255))
    pygame.draw.circle(screen, 'Red', ball_pos, ball_radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] -= movement_amount
            elif event.key == pygame.K_DOWN:
                ball_pos[1] += movement_amount
            elif event.key == pygame.K_LEFT:
                ball_pos[0] -= movement_amount
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] += movement_amount
                
                
    if ball_pos[0] - ball_radius < 0:
        ball_pos[0] = ball_radius
    elif ball_pos[0] + ball_radius > window_size[0]:
        ball_pos[0] = window_size[0] - ball_radius
    if ball_pos[1] - ball_radius < 0:
        ball_pos[1] = ball_radius
    elif ball_pos[1] + ball_radius > window_size[1]:
        ball_pos[1] = window_size[1] - ball_radius            
    
    pygame.display.update()
    pygame.time.wait(16)   
