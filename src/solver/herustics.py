from game.game_logic import logiikka


class Ratkoja:
    "Tähän tulee itse pelin ratkaisija."

    def __init__(self, lauta):
        "Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden"
        self.peli = lauta

    def laske_arvo(self):
        "Laskee kentän arvon"
        lauta = self.peli

        tyhjat_paino = 4.0
        mono_paino = 1.0
        kulma_pit_paino = 10.0
        viereiset_ruudut_paino = 0.0

        tyhjat = self.laske_tyhjat(lauta)
        monotoonisuus = self.laske_mono(lauta)
        havio = self.onko_loppu(lauta)
        kulma_pit = self.laske_kulma_arvo(lauta)
        viereiset = 0  # self.laske_vieresiet_ruudut(lauta)

        return (
            (tyhjat * tyhjat_paino)
            + (monotoonisuus * mono_paino)
            + (kulma_pit * kulma_pit_paino)
            + (viereiset * viereiset_ruudut_paino)
            - (havio)
        )

    def onko_loppu(self, lauta):
        "Katsoo onko peli loppu"
        arvo = 0
        if logiikka.hae_nykyinen_tila(lauta) == "Hävisit pelin!":
            arvo = 20000
        return arvo

    def laske_vieresiet_ruudut(self, lauta):
        "Laskee arvon sen mukaan onko tyhjän ruudun vieressä kaksi samaa arvoa"
        "Auttaa pitämään kentän tyhjänä"
        arvo = 0

        for i in range(len(lauta)):
            for j in range(len(lauta[0])):
                if lauta[i][j] == 0:
                    if i > 0 and i < 3 and lauta[i - 1][j] == lauta[i + 1][j]:
                        arvo += 1
                    if i < len(lauta) - 2 and lauta[i + 1][j] == lauta[i + 2][j]:
                        arvo += 1
                    if j > 0 and j < 3 and lauta[i][j - 1] == lauta[i][j + 1]:
                        arvo += 1
                    if j < len(lauta[0]) - 2 and lauta[i][j + 1] == lauta[i][j + 2]:
                        arvo += 1

        return arvo

    def laske_kulma_arvo(self, lauta):
        "Laskee manattan pituuden suurimmasta arvosta lähimpään nurkkaan"
        kulmat = [(0, 0), (3, 0), (0, 3), (3, 3)]
        korkein_arvo = 0
        korkein_arvo_paikka = None
        for rivi in range(len(lauta)):
            for sarake in range(len(lauta[0])):
                if lauta[rivi][sarake] > korkein_arvo:
                    korkein_arvo = lauta[rivi][sarake]
                    korkein_arvo_paikka = (rivi, sarake)
        # Laskee manhattan pituudet nurkkiin (jos arvo on nurkassa muutetaan arvo 1 koska muuten jaetaan nollalla)
        pituudet_kulmaan = [
            (
                abs(korkein_arvo_paikka[0] - kulma[0])
                + abs(korkein_arvo_paikka[1] - kulma[1])
                if abs(korkein_arvo_paikka[0] - kulma[0])
                + abs(korkein_arvo_paikka[1] - kulma[1])
                != 0
                else 1
            )
            for kulma in kulmat
        ]
        # Ottaa lyhimmän arvon ja palauttaa sen käänteisluvun
        return (1 / min(pituudet_kulmaan)) * (korkein_arvo / 10)

    def laske_tyhjat(self, lauta):
        "laskee tyhjien ruutujen määrän"
        tyhjat = 0
        for y in range(len(lauta)):
            for x in range(len(lauta[0])):
                if lauta[y][x] == 0:
                    tyhjat += 1

        return tyhjat

    def laske_mono(self, lauta):
        "laskee monotoonisuudelle arvon"
        mono_vasen = 0
        mono_ylos = 0

        for i in range(4):
            for j in range(3):
                # Tarkista vaakasuorat rivit
                mono_vasen += lauta[i][j] - lauta[i][j + 1]

                # Tarkista sarakkeet
                mono_ylos += lauta[j][i] - lauta[j + 1][i]

        arvo = mono_vasen + mono_ylos

        return arvo
