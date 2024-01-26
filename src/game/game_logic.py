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

    def hae_nykyinen_tila(self, jatko=False, lauta=None):
        "Tarkistaa olemmeko voittaneet/hävinneet vai jatkuuko peli vielä."
        if lauta:
            if not jatko:  # Tarkistaa jatkuuko peli vai ei jos 2048 on saavutettu
                for i in range(4):  # Jos jostain löytyy 2048 olemme voittaneet
                    for j in range(4):
                        if lauta[i][j] == 2048:
                            return "Sinä voitit!"

                for i in range(4):  # Jos on tyhjää peli on vielä käynnissä
                    for j in range(4):
                        if lauta[i][j] == 0:
                            return "ei"

                # Jos kaikki kohdat ovat täynnä mutta pystymme yhdistämään arvoja peli ei ole vielä ohi
                for i in range(3):
                    for j in range(3):
                        if (
                            lauta[i][j] == lauta[i + 1][j]
                            or lauta[i][j] == lauta[i][j + 1]
                        ):
                            return "ei"

                for j in range(3):
                    if lauta[3][j] == lauta[3][j + 1] or lauta[j][3] == lauta[j + 1][3]:
                        return "ei"

                return "Hävisit pelin!"

        if not jatko:  # Tarkistaa jatkuuko peli vai ei jos 2048 on saavutettu
            for i in range(4):  # Jos jostain löytyy 2048 olemme voittaneet
                for j in range(4):
                    if self.peli_lauta[i][j] == 2048:
                        return "Sinä voitit!"

        for i in range(4):  # Jos on tyhjää peli on vielä käynnissä
            for j in range(4):
                if self.peli_lauta[i][j] == 0:
                    return "ei"

        # Jos kaikki kohdat ovat täynnä mutta pystymme yhdistämään arvoja peli ei ole vielä ohi
        for i in range(3):
            for j in range(3):
                if (
                    self.peli_lauta[i][j] == self.peli_lauta[i + 1][j]
                    or self.peli_lauta[i][j] == self.peli_lauta[i][j + 1]
                ):
                    return "ei"

        for j in range(3):
            if (
                self.peli_lauta[3][j] == self.peli_lauta[3][j + 1]
                or self.peli_lauta[j][3] == self.peli_lauta[j + 1][3]
            ):
                return "ei"

        return "Hävisit pelin!"

    def tiivista(self, lauta=[]):
        """Siirtää kaiken vasempaan reunaan"""

        if len(lauta) > 1:
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

        muuttunut = False

        uusi_lauta = [[0] * 4 for i in range(4)]

        for i in range(4):
            paikka = 0
            for j in range(4):
                if self.peli_lauta[i][j] != 0:
                    uusi_lauta[i][paikka] = self.peli_lauta[i][j]

                    if j != paikka:
                        muuttunut = True
                    paikka += 1
        self.peli_lauta = uusi_lauta

        return muuttunut

    def yhdista(self, lauta=[]):
        """Jos vierekkäisillä ruuduilla on sama arvo yhdistää se ne yhdeksi"""

        if len(lauta) > 1:
            muuttunut = False

            for i in range(4):
                for j in range(3):
                    if lauta[i][j] == lauta[i][j + 1] and lauta[i][j] != 0:
                        lauta[i][j] = lauta[i][j] * 2
                        lauta[i][j + 1] = 0

                        muuttunut = True

            return muuttunut, lauta

        muuttunut = False

        for i in range(4):
            for j in range(3):
                if (
                    self.peli_lauta[i][j] == self.peli_lauta[i][j + 1]
                    and self.peli_lauta[i][j] != 0
                ):
                    self.peli_lauta[i][j] = self.peli_lauta[i][j] * 2
                    self.peli_lauta[i][j + 1] = 0

                    muuttunut = True

        return muuttunut

    def kaanna(self, lauta=[]):
        "Kääntää laudan ylösalaisin vaakatasossa"
        uusi_lauta = [[] for i in range(4)]
        if len(lauta) > 1:
            for i in range(4):
                for j in range(4):
                    uusi_lauta[i].append(lauta[i][3 - j])
            return uusi_lauta

        for i in range(4):
            for j in range(4):
                uusi_lauta[i].append(self.peli_lauta[i][3 - j])
        self.peli_lauta = uusi_lauta

    def vaihda(self, lauta=[]):
        "Vaihtaa rivien ja sarakkeitten paikkaa"
        uus_lauta = [[] for i in range(4)]
        if len(lauta) > 1:
            for i in range(4):
                for j in range(4):
                    uus_lauta[i].append(lauta[j][i])
            return uus_lauta

        for i in range(4):
            for j in range(4):
                uus_lauta[i].append(self.peli_lauta[j][i])
        self.peli_lauta = uus_lauta

    def ylos(self, lauta=[]):
        "Siirtää kaiken ylös"
        if len(lauta) > 1:
            lauta = self.vaihda(lauta)

            muuttunut, lauta = self.vasen(lauta)

            lauta = self.vaihda(lauta)

            return muuttunut, lauta

        self.vaihda()

        muuttunut = self.vasen()

        self.vaihda()

        return muuttunut

    def alas(self, lauta=[]):
        "Siirtää kaiken alas"
        if len(lauta) > 1:  # Tekoälyn lauta
            lauta = self.vaihda(lauta)

            muuttunut, lauta = self.oikea(lauta)

            lauta = self.vaihda(lauta)

            return muuttunut, lauta

        # Oikea pelilauta
        self.vaihda()

        muuttunut = self.oikea()

        self.vaihda()

        return muuttunut

    def vasen(self, lauta=[]):
        "Siirtää kaiken vasemmalle"
        if len(lauta) > 1:
            muuttunut1, lauta = self.tiivista(lauta)

            muuttunut2, lauta = self.yhdista(lauta)

            muuttunut = muuttunut1 or muuttunut2

            temp, lauta = self.tiivista(lauta)

            return muuttunut, lauta

        muuttunut1 = self.tiivista()

        muuttunut2 = self.yhdista()

        muuttunut = muuttunut1 or muuttunut2

        self.tiivista()

        return muuttunut

    def oikea(self, lauta=[]):
        "Siirtää kaiken oikealla"
        if len(lauta):
            lauta = self.kaanna(lauta)

            muuttunut, lauta = self.vasen(lauta)

            lauta = self.kaanna(lauta)

            return muuttunut, lauta

        self.kaanna()

        muuttunut = self.vasen()

        self.kaanna()

        return muuttunut

    def lauta(self):
        "Palauttaa laudan"
        return self.peli_lauta

    def nollaa(self):
        "Nollaa laudan ja lisää kaksi arvoa"
        self.peli_lauta = [[0] * 4 for i in range(4)]

        self.lisaa_arvo()
        self.lisaa_arvo()


logiikka = Logic()
