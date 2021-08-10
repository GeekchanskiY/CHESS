import pygame
from classes import *

pygame.init()
window = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("CHESS")
size = 50

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("See you next time!")
            run = False

    # Draw BG
    pygame.draw.rect(window, pygame.Color(211, 211, 211), (0, 0, 1800, 1000))


    cnt = 0
    for i in range(1, 9):
        for z in range(1, 9):
            if cnt % 2 == 0:
                pygame.draw.rect(window, pygame.Color(50, 50, 50), (size*z, size*i, size, size))
                w = False
            else:
                pygame.draw.rect(window, pygame.Color(255, 255, 255), (size*z, size*i, size, size))
                w = True
            cnt += 1
        cnt -= 1

    pygame.display.update()

pygame.quit()
