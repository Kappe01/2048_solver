import numpy as np
from game.game_logic import logiikka


class Ratkoja:
    "Tähän tulee itse pelin ratkaisija."

    def __init__(self, lauta):
        "Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden"
        self.peli = lauta

    def laske_arvo(self):
        "Laskee kentän arvon"
        lauta = self.peli

        tyhjat_paino = 0.1
        mono_paino = 1.0
        kulma_pit_paino = 1.0
        gradient_paino = 0.5

        tyhjat = self.laske_tyhjat(lauta)
        monotoonisuus = self.laske_mono(lauta)
        havio = self.onko_loppu(lauta)
        kulma_pit = self.laske_kulma_arvo(lauta)
        gradient = self.silea_vietto(lauta)

        return (
            (tyhjat * tyhjat_paino)
            + (monotoonisuus * mono_paino)
            + (kulma_pit * kulma_pit_paino)
            + (gradient * gradient_paino)
            - (havio)
        )

    def silea_vietto(self, lauta):
        "Kannustaa sileää arvojen viettoa vasemmasta yläkulmasta oikeaan alakulmaan"
        lauta = np.array(lauta)
        oikeat_erot = np.abs(lauta[:-1, :-1] - lauta[:-1, 1:])
        ala_erot = np.abs(lauta[:-1, :-1] - lauta[1:, :-1])
        kokonais_ero = np.sum(oikeat_erot) + np.sum(ala_erot)
        return (
            -kokonais_ero
        )  # Palauta negatiivinen arvo, koska pienemmät erot ovat parempia

    def onko_loppu(self, lauta):
        "Katsoo onko peli loppu"
        arvo = 0
        if logiikka.hae_nykyinen_tila(lauta) == "Hävisit pelin!":
            arvo = 20000
        return arvo

    def laske_kulma_arvo(self, lauta):
        "Palauttaa suurinmman laaran arvon jos suurin arvo on kulmassa"
        lauta = np.array(lauta)
        suurin_arvo = np.max(lauta)
        if suurin_arvo == lauta[0][0]:
            return suurin_arvo
        return 0

    def laske_tyhjat(self, lauta):
        "laskee tyhjien ruutujen määrän"
        lauta = np.array(lauta)
        tyhjat = np.count_nonzero(lauta == 0)
        return tyhjat

    def laske_mono(self, lauta):
        "laskee monotoonisuudelle arvon"
        lauta = np.array(lauta)
        mono_vasen = np.sum(np.diff(lauta, axis=1))
        mono_ylos = np.sum(np.diff(lauta, axis=0))

        arvo = mono_vasen + mono_ylos

        return arvo
