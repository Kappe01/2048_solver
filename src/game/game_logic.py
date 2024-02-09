import random


class Logic:
    """2048-pelin logiikka."""

    def __init__(self):
        self.nollaa()

    def lisaa_arvo(self):
        """Lisää lautaan kakkosen 90% todennäköisyydellä ja 10% todennäköisyydellä nelosen."""
        rivi = random.randint(0, 3)
        sarake = random.randint(0, 3)

        while self.peli_lauta[rivi][sarake] != 0:
            rivi = random.randint(0, 3)
            sarake = random.randint(0, 3)

        kaksi_tai_nelja = random.randint(0, 9)

        if kaksi_tai_nelja == 0:  # 10% mahdollisuus että tulee 4 laudalle muuten 2.
            self.peli_lauta[rivi][sarake] = 4
        else:
            self.peli_lauta[rivi][sarake] = 2

    def hae_nykyinen_tila(self, lauta=None):
        "Tarkistaa olemmeko voittaneet/hävinneet vai jatkuuko peli vielä."
        peli = self.peli_lauta

        if lauta:
            peli = lauta

        for i in range(4):  # Jos on tyhjää peli on vielä käynnissä
            for j in range(4):
                if peli[i][j] == 0:
                    return "ei"

        # Jos kaikki kohdat ovat täynnä mutta pystymme yhdistämään arvoja peli ei ole vielä ohi
        for i in range(3):
            for j in range(3):
                if peli[i][j] == peli[i + 1][j] or peli[i][j] == peli[i][j + 1]:
                    return "ei"

        for j in range(3):
            if peli[3][j] == peli[3][j + 1] or peli[j][3] == peli[j + 1][3]:
                return "ei"

        return "Hävisit pelin!"

    def tiivista(self, lauta):
        """Siirtää kaiken vasempaan reunaan"""

        muuttunut = False

        uusi_lauta = [[0] * 4 for i in range(4)]

        for i in range(4):
            paikka = 0
            for j in range(4):
                if lauta[i][j] != 0:
                    uusi_lauta[i][paikka] = lauta[i][j]

                    if j != paikka:
                        muuttunut = True
                    paikka += 1
        lauta = uusi_lauta

        return muuttunut, lauta

    def yhdista(self, lauta):
        """Jos vierekkäisillä ruuduilla on sama arvo yhdistää se ne yhdeksi"""
        muuttunut = False

        for i in range(4):
            for j in range(3):
                if lauta[i][j] == lauta[i][j + 1] and lauta[i][j] != 0:
                    lauta[i][j] = lauta[i][j] * 2
                    lauta[i][j + 1] = 0

                    muuttunut = True

        return muuttunut, lauta

    def kaanna(self, lauta):
        "Kääntää laudan ylösalaisin vaakatasossa"
        uusi_lauta = [[] for i in range(4)]

        for i in range(4):
            for j in range(4):
                uusi_lauta[i].append(lauta[i][3 - j])
        return uusi_lauta

    def vaihda(self, lauta):
        "Vaihtaa rivien ja sarakkeitten paikkaa"
        uus_lauta = [[] for i in range(4)]

        for i in range(4):
            for j in range(4):
                uus_lauta[i].append(lauta[j][i])
        return uus_lauta

    def ylos(self, lauta=[]):
        "Siirtää kaiken ylös"
        peli = self.peli_lauta
        if len(lauta) > 1:
            peli = lauta

        peli = self.vaihda(peli)

        muuttunut, peli = self.vasen(peli)

        peli = self.vaihda(peli)

        if not lauta:
            self.peli_lauta = peli

        return muuttunut, peli

    def alas(self, lauta=[]):
        "Siirtää kaiken alas"
        peli = self.peli_lauta

        if len(lauta) > 1:  # Tekoälyn lauta
            peli = lauta

        peli = self.vaihda(peli)

        muuttunut, peli = self.oikea(peli)

        peli = self.vaihda(peli)

        if not lauta:
            self.peli_lauta = peli

        return muuttunut, peli

    def vasen(self, lauta=[]):
        "Siirtää kaiken vasemmalle"
        peli = self.peli_lauta

        if len(lauta) > 1:
            peli = lauta

        muuttunut1, peli = self.tiivista(peli)

        muuttunut2, peli = self.yhdista(peli)

        muuttunut = muuttunut1 or muuttunut2

        temp, peli = self.tiivista(peli)

        if not lauta:
            self.peli_lauta = peli

        return muuttunut, peli

    def oikea(self, lauta=[]):
        "Siirtää kaiken oikealla"
        peli = self.peli_lauta
        if len(lauta) > 1:
            peli = lauta

        peli = self.kaanna(peli)

        muuttunut, peli = self.vasen(peli)

        peli = self.kaanna(peli)

        if not lauta:
            self.peli_lauta = peli

        return muuttunut, peli

    def lauta(self):
        "Palauttaa laudan"
        return self.peli_lauta

    def nollaa(self):
        "Nollaa laudan ja lisää kaksi arvoa"
        self.peli_lauta = [[0] * 4 for i in range(4)]

        self.lisaa_arvo()
        self.lisaa_arvo()


logiikka = Logic()
