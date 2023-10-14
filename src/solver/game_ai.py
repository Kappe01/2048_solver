from game.game_logic import logiikka

PARAS_TILANNE = [[2**16,2**15,2**14,2**13],
                 [2**9,2**10,2**11,2**12],
                 [2**8,2**7,2**6,2**5],
                 [2**1,2**2,2**3,2**4]] #Tällä lasketaan laudan arvot

class Ratkoja:
    'Tähän tulee itse pelin ratkaisija. '
    def __init__(self):
        'Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden'
        self.syvyys = 2
        self.peli = logiikka.lauta()

    def aseta_syvyys(self, syvyys):
        #self.syvyys = syvyys
        pass
    def laske_arvo(self, lauta):
        'Laskee kentän arvon joka myöhemmin toimii noden arvona'
        'Heurestiikka on vielä kehitteillä'
        arvo = 0
        tyhjat = 0
        for y in range(len(lauta)):
            for x in range(len(lauta[0])):
                if lauta[y][x] == 0:
                    tyhjat += 1
                arvo += lauta[y][x]
        return arvo + tyhjat
    
    def seuraava_siirto(self):
        paras_siirto = ''
        paras_arvo = 0
        for siirto in ['ylos', 'alas', 'vasen', 'oikea']:
            arvo = self.laske_arvot(siirto)
            if arvo > paras_arvo:
                paras_arvo = arvo
                paras_siirto = siirto
        self.peli = logiikka.lauta()
        return paras_siirto

    def laske_arvot(self, siirto):
        muuttunut = False
        if siirto == 'vasen':
            muuttunut, uusi_lauta = logiikka.vasen(self.peli)
        elif siirto == 'oikea':
            muuttunut, uusi_lauta = logiikka.oikea(self.peli)
        elif siirto == 'alas':
            muuttunut, uusi_lauta = logiikka.alas(self.peli)
        elif siirto == 'ylos':
            muuttunut, uusi_lauta = logiikka.ylos(self.peli)
        if not muuttunut:
            return 0
        return self.luo_arvo(uusi_lauta, 0, self.syvyys)
    
    def luo_arvo(self, lauta, nykyinen_syvyys, syvyys_raja):
        if nykyinen_syvyys == syvyys_raja:
            return self.laske_arvo(lauta)
        arvo = 0
        for y in range(len(lauta)):
            for x in range(len(lauta[0])):
                if lauta[y][x] == 0:
                    uusi_lauta2 = lauta
                    uusi_lauta2[y][x] = 2
                    arvo2 = self.laske_siirron_arvo(uusi_lauta2, nykyinen_syvyys, syvyys_raja)
                    arvo = arvo + (0.9 * arvo2)

                    uusi_lauta4 = lauta
                    uusi_lauta4[y][x] = 4
                    arvo4 = self.laske_siirron_arvo(uusi_lauta4, nykyinen_syvyys, syvyys_raja)
                    arvo = arvo + (0.1*arvo4)
        return arvo
    
    def laske_siirron_arvo(self, lauta, nykyinen_syvyys, syvyys_raja):
        arvo = 0
        muuttunut = False
        for siirto in ['ylos', 'alas', 'vasen', 'oikea']:
            if siirto == 'vasen':
                muuttunut, uusi_lauta = logiikka.vasen(lauta)
            elif siirto == 'oikea':
                muuttunut, uusi_lauta = logiikka.oikea(lauta)
            elif siirto == 'alas':
                muuttunut, uusi_lauta = logiikka.alas(lauta)
            elif siirto == 'ylos':
                muuttunut, uusi_lauta = logiikka.ylos(lauta)
            if muuttunut:
                siirron_arvo = self.luo_arvo(uusi_lauta, nykyinen_syvyys+1, syvyys_raja)
                arvo = max([arvo, siirron_arvo])

        return arvo

ratkoja = Ratkoja()