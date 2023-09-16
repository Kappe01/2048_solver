import random


class Logic:
    '''2048-pelin logiikka.'''

    def __init__(self):
        self.peli_lauta = [[0]*4 for i in range(4)]  # Luo tyhjän laudan

        self.lisaa_arvo()
        self.lisaa_arvo()  # Lisätään kaksi arvoa lautaan

    def lisaa_arvo(self):
        '''Lisää lautaan kakkosen 90% todennäköisyydellä ja 10% todennäköisyydellä nelosen.'''
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

    def get_current_state(self):
        'Tarkistaa olemmeko voittaneet/hävinneet vai jatkuuko peli vielä.'

        for i in range(4):  # Jos jostain löytyy 2048 olemme voittaneet
            for j in range(4):
                if self.peli_lauta[i][j] == 2048:
                    return 'Sinä voitit!'

        for i in range(4):  # Jos on tyhjää peli on vielä käynnissä
            for j in range(4):
                if self.peli_lauta[i][j] == 0:
                    return 'ei'

        # Jos kaikki kohdat ovat täynnä mutta pystymme yhdistämään arvoja peli ei ole vielä ohi
        for i in range(3):
            for j in range(3):
                if self.peli_lauta[i][j] == self.peli_lauta[
                    i + 1][j] or self.peli_lauta[i][j] == self.peli_lauta[i][j + 1]:
                    return 'ei'

        for j in range(3):
            if self.peli_lauta[3][j] == self.peli_lauta[3][
                j + 1] or self.peli_lauta[j][3] == self.peli_lauta[j + 1][3]:
                return 'ei'

        # else we have lost the game
        return 'Hävisit pelin!'

    def tiivista(self):
        '''Siirtää kaiken vasempaan reunaan'''

        muuttunut = False

        uusi_lauta = [[0]*4 for i in range(4)]

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

    def yhdista(self):
        '''Jos vierekkäisillä ruuduilla on sama arvo yhdistää se ne yhdeksi'''

        muuttunut = False

        for i in range(4):
            for j in range(3):
                if self.peli_lauta[i][j] == self.peli_lauta[i][j + 1] and self.peli_lauta[i][j] != 0:

                    self.peli_lauta[i][j] = self.peli_lauta[i][j] * 2
                    self.peli_lauta[i][j + 1] = 0

                    muuttunut = True

        return muuttunut

    def kaanna(self):
        'Kääntää laudan ylösalaisin vaakatasossa'
        uusi_lauta = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                uusi_lauta[i].append(self.peli_lauta[i][3 - j])
        self.peli_lauta = uusi_lauta

    def vaihda(self):
        'Vaihtaa rivien ja sarakkeitten paikkaa'
        uus_lauta = [[] for i in range(4)]
        for i in range(4):
            for j in range(4):
                uus_lauta[i].append(self.peli_lauta[j][i])
        self.peli_lauta = uus_lauta

    def ylos(self):
        'Siirtää kaiken ylös'
        self.vaihda()

        muuttunut = self.vasen()

        self.vaihda()

        return muuttunut

    def alas(self):
        'Siirtää kaiken alas'
        self.vaihda()

        muuttunut = self.oikea()

        self.vaihda()

        return muuttunut

    def vasen(self):
        'Siirtää kaiken vasemmalle'
        muuttunut1 = self.tiivista()

        muuttunut2 = self.yhdista()

        muuttunut = muuttunut1 or muuttunut2

        self.tiivista()

        return muuttunut

    def oikea(self):
        'Siirtää kaiken oikealla'
        self.kaanna()

        muuttunut = self.vasen()

        self.kaanna()

        return muuttunut

    def lauta(self):
        'Palauttaa laudan'
        return self.peli_lauta