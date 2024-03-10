import pygame

pygame.init()
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
is_red = True
x = 30
y = 30
ball_radius = 25

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_red = not is_red
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20

        x = max(ball_radius, min(x, screen_width - ball_radius))
        y = max(ball_radius, min(y, screen_height - ball_radius))
        
        screen.fill((255, 255, 255))
        if is_red: color = (255, 0, 0)
        
        pygame.draw.circle(screen, color, (x, y), ball_radius)
        
        pygame.display.flip()
        clock.tick(60)

#square