import pygame

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
dark_red = (153, 0, 0)
dark_blue = (0, 0, 153)
dark_green = (0, 153, 0)

display_surface = pygame.display.set_mode((1180, 620))
czcionka = "AutourOne-Regular.otf"
my_small_font = pygame.font.Font(czcionka, 32)
my_big_font = pygame.font.Font(czcionka, 37)
smallest_font = pygame.font.Font(czcionka, 26)
nazwa_input = ""

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if len(nazwa_input) > 13:
                nazwa_input = nazwa_input[:-1]
            if event.key == pygame.K_BACKSPACE:
                nazwa_input = nazwa_input[:-1]
            else:
                nazwa_input += event.unicode
    myszka = pygame.mouse.get_pos()

    display_surface.fill(white)
    pygame.draw.rect(display_surface, black, (270, 140, 600, 300))
    pygame.draw.rect(display_surface, white, (400, 270, 330, 50))
    naglowek = my_big_font.render("Podaj nazwę użytkownika", True, dark_green)
    display_surface.blit(naglowek, (285, 170))
    if 490 + 150 > myszka[0] > 150 and 350 + 40 > myszka[1] > 350:
        pygame.draw.rect(display_surface, green, (490, 350, 150, 40))
    else:
        pygame.draw.rect(display_surface, dark_green, (490, 350, 150, 40))

    napis_enter = smallest_font.render("ENTER", True, black)
    display_surface.blit(napis_enter, (520, 355))
    text_surface = my_small_font.render(nazwa_input, True, black)
    display_surface.blit(text_surface, (405, 280))


    pygame.display.flip()

