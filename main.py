import pygame
from classes import *
import os

img_folder = (os.path.abspath("images/alpha/"))

# game init and window options
pygame.init()
window = pygame.display.set_mode((1800, 1000))
window.fill((211, 211, 211))
pygame.display.set_caption("CHESS")

size = 80
ft = 0
coord_list = []
run = True

white_pawn_img = pygame.image.load(os.path.abspath("images/alpha/wP.png")).convert_alpha()
white_king_img = pygame.image.load(os.path.abspath("images/alpha/wK.png")).convert_alpha()
white_queen_img = pygame.image.load(os.path.abspath("images/alpha/wQ.png")).convert_alpha()
white_bishop_img = pygame.image.load(os.path.abspath("images/alpha/wB.png")).convert_alpha()
white_knight_img = pygame.image.load(os.path.abspath("images/alpha/wN.png")).convert_alpha()
white_rook_img = pygame.image.load(os.path.abspath("images/alpha/wR.png")).convert_alpha()

black_pawn_img = pygame.image.load(os.path.abspath("images/alpha/bP.png")).convert_alpha()
black_king_img = pygame.image.load(os.path.abspath("images/alpha/bK.png")).convert_alpha()
black_queen_img = pygame.image.load(os.path.abspath("images/alpha/bQ.png")).convert_alpha()
black_bishop_img = pygame.image.load(os.path.abspath("images/alpha/bB.png")).convert_alpha()
black_knight_img = pygame.image.load(os.path.abspath("images/alpha/bN.png")).convert_alpha()
black_rook_img = pygame.image.load(os.path.abspath("images/alpha/bR.png")).convert_alpha()


def draw_board():
    cnt = 0
    for i in range(1, 9):
        for z in range(1, 9):
            if cnt % 2 == 0:
                pygame.draw.rect(window, pygame.Color(50, 50, 50), (size*z, size*i, size, size))
                w = False
            else:
                pygame.draw.rect(window, pygame.Color(255, 255, 255), (size*z, size*i, size, size))
                w = True
            if ft == 0:
                coord_list.append({size * z, size * i})
            cnt += 1
        cnt -= 1


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("See you next time!")
            run = False

    draw_board()
    ft = 1
    window.blit(white_pawn_img, (80, 560))
    window.blit(white_pawn_img, (160, 560))
    window.blit(white_pawn_img, (240, 560))
    window.blit(white_pawn_img, (320, 560))
    window.blit(white_pawn_img, (400, 560))
    window.blit(white_pawn_img, (480, 560))
    window.blit(white_pawn_img, (560, 560))
    window.blit(white_pawn_img, (640, 560))

    print(pygame.mouse.get_pos())
    # Updating display
    pygame.display.update()

pygame.quit()
