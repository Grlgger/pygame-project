import pygame
import random

pygame.init()
best_score = 0
music = pygame.mixer.Sound("game_music.mp3")
lose_music = pygame.mixer.Sound("lose.mp3")
hero_images = [pygame.transform.scale(pygame.image.load('hero1.png'), (76, 120)),
               pygame.transform.scale(pygame.image.load('hero3.png'), (76, 120))]
stars = []

def start_screen():
    global best_score

    s = pygame.mixer.Sound("start_screen.mp3")
    s.play()

    size = 1920, 1080

    screen = pygame.display.set_mode(size)
    font = pygame.font.Font('retro-land-mayhem.ttf', 80)
    fon = pygame.image.load('fon.jpg')
    screen.blit(fon, (0, 0))
    floor = pygame.transform.scale(pygame.image.load('floor.jpg'), (1920, 455))
    screen.blit(floor, (0, 760))

    hero = pygame.transform.scale(pygame.image.load('hero1.png'), (76, 120))
    hero_rect = hero.get_rect(midbottom=(400, 760)).inflate(5, 5)

    rum = pygame.transform.scale(pygame.image.load('rum.png'), (30, 70))
    rum_rect = rum.get_rect(midbottom=(500, 760))

    screen.blit(hero, hero_rect)
    screen.blit(rum, rum_rect)

    text_1 = font.render(f"""Welcome to""", False, 'white')
    text_2 = font.render(f"""The Search of Jack Sparrow's Rum!""", False, 'white')
    text_3 = font.render(f"""Press "Space" to start""", False, 'white')

    screen.blit(text_1, (700, 100))
    screen.blit(text_2, (100, 220))
    screen.blit(text_3, (440, 340))

    for i in range(40):
        star = pygame.image.load('star.png')
        stars.append([star, star.get_rect(midbottom=(random.randint(30, 1900), random.randint(30, 500)))])
    for star, rect in stars:
        screen.blit(star, rect)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                s.stop()
                new_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hero_rect.collidepoint(event.pos):
                    captain_jack_sparrow = pygame.mixer.Sound("captain_jack_sparrow_quote.mp3")
                    captain_jack_sparrow.play()
        pygame.display.update()
    pygame.quit()
