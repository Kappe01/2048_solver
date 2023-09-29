import pygame
from math import log2
from game.game_logic import logiikka
from solver.game_solver import ratkoja
import threading
import time


class UI:
    '''Tähän tulee pygamella toteutettu graafinen käyttöliittymä'''

    def __init__(self):
        'Alustaa pelin'
        pygame.init()

        self.lataa_arvot()
        self.uusi_peli()

        self.korkeus = len(self.peli)
        self.leveys = len(self.peli[0])
        self.skaala = self.arvot[0].get_width()

        self.naytto = pygame.display.set_mode((self.korkeus * self.skaala, (self.leveys*self.skaala) + self.skaala))

        self.fontti = pygame.font.SysFont('Arial', 24)

        self.jatka = False
        self.AI = False

        pygame.display.set_caption('2048')

        self.silmukka()

    def lataa_arvot(self):
        'Lataa peli arvojen kuvat'
        self.arvot = []

        for arvo in ['0','2','4','8','16','32','64','128','256','512','1024','2048']:
            self.arvot.append(pygame.image.load(f'./Dokumentaatio/Kuvat/{arvo}.png'))


    def uusi_peli(self):
        'Aloittaa uuden pelin.'
        logiikka.nollaa()
        self.peli = logiikka.lauta()

    def silmukka(self):
        'Pitää pelin käynnissä'
        while True:
            self.tapahtumat()
            self.paivita()

    def tapahtumat(self):
        'Käy läpi tapahtumat ja tekee tarvittavat toimenpiteet'
        for tapahtuma in pygame.event.get():
            
            if tapahtuma.type == pygame.KEYDOWN:
                if not self.AI: # Jos ohjelmaa suoritetaan AIn kanssa ei voi siirtää itse ruutua
                    if tapahtuma.key == pygame.K_LEFT:
                        muuttunut = logiikka.vasen()
                        if muuttunut:
                            logiikka.lisaa_arvo()
                    if tapahtuma.key == pygame.K_RIGHT:
                        muuttunut = logiikka.oikea()
                        if muuttunut:
                            logiikka.lisaa_arvo()
                    if tapahtuma.key == pygame.K_UP:
                        muuttunut = logiikka.ylos()
                        if muuttunut:
                            logiikka.lisaa_arvo()
                    if tapahtuma.key == pygame.K_DOWN:
                        muuttunut = logiikka.alas()
                        if muuttunut:
                            logiikka.lisaa_arvo()

                if tapahtuma.key == pygame.K_F2:
                    self.AI = False
                    self.uusi_peli()
                if tapahtuma.key == pygame.K_RETURN:
                    self.AI = True
                    #t1 = threading.Thread(target=self.ai)
                    #t1.start()
                    self.ai()
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()

            if tapahtuma.type == pygame.QUIT:
                exit()

        self.peli = logiikka.lauta()

    def paivita(self):
        'Päivittää näytöm'
        self.naytto.fill((176,224,230)) 

        for y in range(self.korkeus):
            for x in range(self.leveys):
                numero = self.peli[y][x]
                self.naytto.blit(self.arvot[int(log2(numero)) if numero != 0 else 0], (x * self.skaala, y * self.skaala))

        if logiikka.get_current_state(self.jatka) == 'Sinä voitit!':
            self.AI = False
            print('gg')

        if logiikka.get_current_state() == 'Hävisit pelin!':
            self.AI = False
            print('bg')

        pygame.display.flip() 

    def ai(self):
        while self.AI:
            ratkoja.aloita_alusta()
            ratkoja.tee_nodet()
            siirto = ratkoja.seuraava_siirto()

            muuttunut = False

            if siirto == 'vasen':
                muuttunut = logiikka.vasen()
            elif siirto == 'oikea':
                muuttunut = logiikka.oikea()
            elif siirto == 'alas':
                muuttunut = logiikka.alas()
            elif siirto == 'ylos':
                muuttunut = logiikka.ylos()
            
            if muuttunut:
                logiikka.lisaa_arvo()

            self.tapahtumat()
            self.paivita()

            time.sleep(0.1)





aloita = UI()

