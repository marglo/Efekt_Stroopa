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
X = 350
Y = 265
Z = 600
czcionka = "AutourOne-Regular.otf"
display_surface = pygame.display.set_mode((1180, 620))

class Wynik:
    def __init__(self, nazwa_uzytkownika, czas):
        self.nazwa_uzytkownika = nazwa_uzytkownika
        self.czas = czas
        self.font = pygame.font.Font(czcionka, 24)  # import pandas as pd
        self.pole_uzytkownik = self.font.render(nazwa_uzytkownika, True, black, dark_green)
        self.uzytkownikRect = self.pole_uzytkownik.get_rect()
        self.font = pygame.font.Font(czcionka, 24)
        self.pole_czas = self.font.render(str(czas), True, black, dark_green)
        self.czasRect = self.pole_czas.get_rect()
        moja_tabela.dodaj_wynik(self)

    def zapisz_wynik(nazwa_uzytkownika, czas):
        plik = open("wyniki.txt", "a")
        plik.write("\n" + nazwa_uzytkownika + " " + czas)
        plik.close()


class Tabela:
    tabela_wynikow = []

    def dodaj_wynik(self, wynik):
        self.tabela_wynikow.append(wynik)

    def wczytaj_wyniki(self):
        plik = open('wyniki.txt')
        tabela_wejscie = plik.readlines()
        plik.close()

        for i in tabela_wejscie:
            i = i.split()
            Wynik(i[0], int(i[1]))
        self.tabela_wynikow = sorted(self.tabela_wynikow, key=lambda i: i.czas)

moja_tabela = Tabela()
moja_tabela.wczytaj_wyniki()

def wyswietlanie_tabeli():
    while True:
        display_surface.fill(white)
        odstep = 0
        font = pygame.font.Font(czcionka, 30)
        tekst_nazwa = font.render("Nazwa użytkownika", True, black)
        display_surface.blit(tekst_nazwa, (200, 200))
        tekst_czas = font.render("Czas [s]", True, black)
        display_surface.blit(tekst_czas, (750, 200))
        pygame.draw.line(display_surface, black, (150, 190), (1000, 190))

        for wynik in moja_tabela.tabela_wynikow[:5]:
            wynik.uzytkownikRect.center = (X, Y + odstep)
            odstep += 50
            display_surface.blit(wynik.pole_uzytkownik, wynik.uzytkownikRect)
            pygame.draw.line(display_surface, black, (150, 190 + odstep), (1000, 190 + odstep))
        pygame.draw.line(display_surface, black, (150, 240 + (50 * min(5, len(moja_tabela.tabela_wynikow)))),
                         (1000, 240 + (50 * min(5, len(moja_tabela.tabela_wynikow)))))
        pygame.draw.line(display_surface, black, (150, 190),
                         (150, 240 + (50 * min(5, len(moja_tabela.tabela_wynikow)))))
        pygame.draw.line(display_surface, black, (1000, 190),
                         (1000, 240 + (50 * min(5, len(moja_tabela.tabela_wynikow)))))
        pygame.draw.line(display_surface, black, (600, 190),
                         (600, 240 + (50 * min(5, len(moja_tabela.tabela_wynikow)))))

        odstep2 = 0
        for wynik in moja_tabela.tabela_wynikow[:5]:
            wynik.czasRect.center = (X + 450, Y + odstep2)
            odstep2 += 50
            display_surface.blit(wynik.pole_czas, wynik.czasRect)

        czcionka_napis_glowny = pygame.font.Font(czcionka, 130)
        napis_glowny = czcionka_napis_glowny.render("Rekordy", True, black)
        display_surface.blit(napis_glowny, (270, 25))

        myszka = pygame.mouse.get_pos()

        if 180 + 800 > myszka[0] > 180 and 500 + 60 > myszka[1] > 500:
            pygame.draw.rect(display_surface, green, (180, 500, 800, 60))
        else:
            pygame.draw.rect(display_surface, dark_green, (180, 500, 800, 60))

        czcionka_wroc = pygame.font.Font(czcionka, 30)
        napis_wroc = czcionka_wroc.render("Wróć do menu", True, black)
        display_surface.blit(napis_wroc, (460, 510))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()

wyswietlanie_tabeli()
