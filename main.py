import pygame
import math

pygame.init()

width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("13-kąt")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

width_polygon, height_polygon = 150, 150

center = (width // 2, height // 2, 150)

rotation = 0

# Funkcja rysująca wielokąt
def draw_polygon(center, width, height, rotation):
    points = []
    num_sides = 13
    angle = math.radians(360 / num_sides)

    for i in range(num_sides):
        x = center[0] + width * math.cos(i * angle + math.radians(rotation))
        y = center[1] + height * math.sin(i * angle + math.radians(rotation))
        points.append((x, y))

    pygame.draw.polygon(window, BLACK, points, 2)

running = True
while running:
    window.fill(WHITE)
    
    draw_polygon(center, width_polygon, height_polygon, rotation)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                width_polygon //= 2
                height_polygon //= 2
            elif event.key == pygame.K_2:
                width_polygon = int(width_polygon * 1.5)
                height_polygon = int(height_polygon * 1.5)
                rotation += 45
            elif event.key == pygame.K_3:
                width_polygon, height_polygon = 70, 200
                rotation += 180
            elif event.key == pygame.K_4:
                width_polygon += 40
                height_polygon += 40
                rotation += 45
            elif event.key == pygame.K_5:
                width_polygon *= 2
                height_polygon //= 3
            elif event.key == pygame.K_6:
                rotation += 70
                width_polygon *= 2
                height_polygon *= 2
            elif event.key == pygame.K_7:
                width_polygon, height_polygon = 70, 200
                rotation += 270
            elif event.key == pygame.K_8:
                width_polygon *= 2
                height_polygon //= 3
                rotation += 45
            elif event.key == pygame.K_9:
                rotation += 180
                width_polygon *= 2
                height_polygon *= 2

    pygame.display.flip()

pygame.quit()
