
# OGARNIJ WYŚWIETLANIE GRAFIKI ##
import pygame


pygame.init()
clock = pygame.time.Clock()

# Define resolution
display_height = 620
display_width = 1180
main_screen = pygame.display.set_mode((1180, 620))
pygame.display.set_caption('Efekt Stroopa')


# Define colors as variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (153, 0, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 153)
green = (0, 255, 0)
dark_green = (0, 153, 0)

# Load and display images
main_screen_logo = pygame.image.load('mainscreenlogo.png')


def logo(x, y):
    main_screen.blit(main_screen_logo, (x, y))


x = (display_width * 0, 45)
y = (display_height * 0, 8)

# Define text objects
def text_objects(text, font):
    TextSurf = font.render(text, True, black)
    return TextSurf, TextSurf.get_rect()

# Game intro
def intro_screen():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        main_screen.fill(white)
        title_text = pygame.font.Font('C:\Windows\Fonts\COOPBL.ttf', 115)
        TextSurf, TextRect = text_objects('Efekt Stroopa', title_text)
        TextRect.center = ((display_width / 2), (display_height / 5))
        main_screen.blit(TextSurf, TextRect)

        graj_jako_eksperyment = pygame.draw.rect(main_screen, dark_green, (190, 220, 800, 60))
        graj_dla_rozrywki = pygame.draw.rect(main_screen, dark_green, (190, 300, 800, 60))
        informacja_o_eksperymencie = pygame.draw.rect(main_screen, dark_green, (190, 380, 800, 60))
        lista_wyników = pygame.draw.rect(main_screen, dark_green, (190, 460, 800, 60))

        mouse = pygame.mouse.get_pos()


        #Interakcja przycisku 1

        if 190 + 800 > mouse[0] > 190 and 220 + 60 > mouse[1] > 220:
            pygame.draw.rect(main_screen, green, (190, 220, 800, 60))
        else:
            pygame.draw.rect(main_screen, dark_green, (190, 220, 800, 60))

        button_description = pygame.font.Font("C:\Windows\Fonts\COOPBL.ttf", 20)
        textSurf, textRect = text_objects(("Graj jako eksperyment"), button_description)
        textRect.center = ((190 + (800 / 2)), (220 + (60 / 2)))
        main_screen.blit(textSurf, textRect)



        #Interakcja przycisku 2
        if 190 + 800 > mouse[0] > 190 and 300 + 60 > mouse[1] > 300:
            pygame.draw.rect(main_screen, green, (190, 300, 800, 60))
        else:
            pygame.draw.rect(main_screen, dark_green, (190, 300, 800, 60))

        button_description = pygame.font.Font("C:\Windows\Fonts\COOPBL.ttf", 20)
        textSurf, textRect = text_objects(("Graj dla rozrywki"), button_description)
        textRect.center = ((190 + (800 / 2)), (300 + (60 / 2)))
        main_screen.blit(textSurf, textRect)



        #Interakcja przycisku 3
        if 190 + 800 > mouse[0] > 190 and 380 + 60 > mouse[1] > 380:
            pygame.draw.rect(main_screen, green, (190, 380, 800, 60))
        else:
            pygame.draw.rect(main_screen, dark_green, (190, 380, 800, 60))

        button_description = pygame.font.Font("C:\Windows\Fonts\COOPBL.ttf", 20)
        textSurf, textRect = text_objects(("Informacje o eksperymencie"), button_description)
        textRect.center = ((190 + (800 / 2)), (380 + (60 / 2)))
        main_screen.blit(textSurf, textRect)



        #Interakcja przycisku 4
        if 190 + 800 > mouse[0] > 190 and 460 + 60 > mouse[1] > 460:
            pygame.draw.rect(main_screen, green, (190, 460, 800, 60))
        else:
            pygame.draw.rect(main_screen, dark_green, (190, 460, 800, 60))

        button_description = pygame.font.Font("C:\Windows\Fonts\COOPBL.ttf", 20)
        textSurf, textRect = text_objects(("Tabela wyników"), button_description)
        textRect.center = ((190 + (800 / 2)), (460 + (60 / 2)))
        main_screen.blit(textSurf, textRect)


        pygame.display.update()


intro_screen()
pygame.quit()
quit()
