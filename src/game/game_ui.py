import pygame
from math import log2
from game.game_logic import logiikka
from solver.expectimax import hae_siirto, Node
import time


class UI:
    """Tähän tulee pygamella toteutettu graafinen käyttöliittymä"""

    def __init__(self):
        "Alustaa pelin"
        pygame.init()

        self.lataa_arvot()
        self.uusi_peli()

        self.korkeus = len(self.peli)
        self.leveys = len(self.peli[0])
        self.skaala = self.arvot[0].get_width()

        self.naytto = pygame.display.set_mode(
            (self.korkeus * self.skaala, (self.leveys * self.skaala) + self.skaala - 50)
        )

        self.fontti = pygame.font.SysFont("Arial", 24)

        self.jatka = False
        self.AI = False

        pygame.display.set_caption("2048")

        self.silmukka()

    def lataa_arvot(self):
        "Lataa peli arvojen kuvat"
        self.arvot = []

        for arvo in [
            "0",
            "2",
            "4",
            "8",
            "16",
            "32",
            "64",
            "128",
            "256",
            "512",
            "1024",
            "2048",
            "4096",
            "8192",
            "16384",
        ]:
            self.arvot.append(pygame.image.load(f"./Dokumentaatio/Kuvat/{arvo}.png"))

    def uusi_peli(self):
        "Aloittaa uuden pelin."
        logiikka.nollaa()
        self.peli = logiikka.lauta()
        self.tulos = 0

    def silmukka(self):
        "Pitää pelin käynnissä"
        while True:
            self.tapahtumat()
            self.paivita()

    def tapahtumat(self):
        "Käy läpi tapahtumat ja tekee tarvittavat toimenpiteet"
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if (
                    not self.AI
                ):  # Jos ohjelmaa suoritetaan AIn kanssa ei voi siirtää itse ruutua
                    if tapahtuma.key == pygame.K_LEFT:
                        muuttunut, peli, self.tulos = logiikka.vasen(self.tulos)
                        if muuttunut:
                            logiikka.lisaa_arvo()
                    if tapahtuma.key == pygame.K_RIGHT:
                        muuttunut, peli, self.tulos = logiikka.oikea(self.tulos)
                        if muuttunut:
                            logiikka.lisaa_arvo()
                    if tapahtuma.key == pygame.K_UP:
                        muuttunut, peli, self.tulos = logiikka.ylos(self.tulos)
                        if muuttunut:
                            logiikka.lisaa_arvo()
                    if tapahtuma.key == pygame.K_DOWN:
                        muuttunut, peli, self.tulos = logiikka.alas(self.tulos)
                        if muuttunut:
                            logiikka.lisaa_arvo()

                if tapahtuma.key == pygame.K_F2:
                    self.AI = False
                    self.uusi_peli()
                if tapahtuma.key == pygame.K_RETURN:
                    if self.AI == True:
                        self.AI = False
                    else:
                        self.AI = True
                    self.ai()
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()

            if tapahtuma.type == pygame.QUIT:
                exit()

        self.peli = logiikka.lauta()

    def paivita(self):
        "Päivittää näytön"

        self.naytto.fill((176, 224, 230))
        # Laittaa ohjeet näytön alareunaan

        tulos = self.fontti.render(f"Pisteet: {self.tulos}", True, (0, 0, 0))

        pygame.draw.rect(
            self.naytto,
            (255, 255, 255),
            (0, 0, tulos.get_width(), tulos.get_height()),
        )

        self.naytto.blit(tulos, (0, 0))

        teksti = self.fontti.render(
            "F2 = Uusi peli     Enter = Käynnistä AI", True, (0, 0, 0)
        )
        self.naytto.blit(
            teksti, (25, self.korkeus * self.skaala + 10 + tulos.get_height())
        )
        teksti = self.fontti.render("ESC = Lopeta", True, (0, 0, 0))
        self.naytto.blit(
            teksti, (25, self.korkeus * self.skaala + 40 + tulos.get_height())
        )

        # Piirtää itse pelikentän
        for y in range(self.korkeus):
            for x in range(self.leveys):
                numero = self.peli[y][x]
                self.naytto.blit(
                    self.arvot[int(log2(numero)) if numero != 0 else 0],
                    (x * self.skaala, y * self.skaala + teksti.get_height()),
                )

        if logiikka.hae_nykyinen_tila() == "Hävisit pelin!":
            self.AI = False
            teksti = self.fontti.render("Hävisit pelin!", True, (0, 0, 0))
            teksti_x = self.skaala * self.leveys / 2 - teksti.get_width() / 2
            teksti_y = self.skaala * self.korkeus / 2 - teksti.get_height() / 2
            pygame.draw.rect(
                self.naytto,
                (255, 255, 255),
                (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()),
            )
            self.naytto.blit(teksti, (teksti_x, teksti_y))
        pygame.display.flip()

    def ai(self):
        "Pyröittää tekoälyä"
        while self.AI:
            siirto = hae_siirto(Node(self.peli))  # hakee seuraavan siirron
            muuttunut = False

            if siirto == "vasen":
                muuttunut, peli, self.tulos = logiikka.vasen(self.tulos)
            elif siirto == "oikea":
                muuttunut, peli, self.tulos = logiikka.oikea(self.tulos)
            elif siirto == "alas":
                muuttunut, peli, self.tulos = logiikka.alas(self.tulos)
            elif siirto == "ylos":
                muuttunut, peli, self.tulos = logiikka.ylos(self.tulos)

            if muuttunut:
                logiikka.lisaa_arvo()

            self.tapahtumat()
            self.paivita()

            time.sleep(0.1)
