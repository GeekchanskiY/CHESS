import pygame
from classes import *

pygame.init()
window = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("CHESS")

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("See you next time!")
            run = False

    # Draw BG
    pygame.draw.rect(window, pygame.Color(211, 211, 211), (0, 0, 1200, 1000))
    pygame.display.update()

pygame.quit()
