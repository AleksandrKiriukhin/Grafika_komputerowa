import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

run = True
while run:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 0), (300, 300), 75)
    
    rect_x = 300 - 40  
    rect_y = 300 - 40  
    pygame.draw.rect(screen, (255, 255, 0), (rect_x, rect_y, 80, 80))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()
