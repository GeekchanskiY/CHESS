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
            run = False
            print(123)
    print(pygame.mouse.get_pos())
    print(pygame.mouse.get_pressed())

pygame.quit()
