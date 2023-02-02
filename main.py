import pygame
import random

pygame.init()
best_score = 0
music = pygame.mixer.Sound("game_music.mp3")
lose_music = pygame.mixer.Sound("lose.mp3")
hero_images = [pygame.transform.scale(pygame.image.load('hero1.png'), (76, 120)),
               pygame.transform.scale(pygame.image.load('hero3.png'), (76, 120))]
stars = []

