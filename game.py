import pygame
import sys

pygame.init()

screen_width = 300
screen_height = 300

blue = (0, 0, 255)
brown = (200, 150, 100)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

running = True
while running:  # need this line to be able to close code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(blue)

    rectangle_height = 200
    pygame.draw.rect(screen, brown, (0, 50, screen_width, rectangle_height))

    pygame.display.flip()

pygame.quit()
sys.exit()