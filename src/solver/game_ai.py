from game.game_logic import logiikka


class Ratkoja:
    'Tähän tulee itse pelin ratkaisija. '

    def __init__(self):
        'Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden'
        self.syvyys = 2
        self.peli = logiikka.lauta()

    def aseta_syvyys(self, syvyys):
        'Asettaa syvyyden'
        self.syvyys = syvyys
        return self.syvyys

    def laske_arvo(self, lauta, siirto):
        'Laskee kentän arvon'
        # Eri heurististen arvojen painot
        laudan_arvo_paino = 0.0
        tyhjat_paino = 0.2
        mono_paino = 0.1
        kulma_pit_paino = 1.0
        viereiset_ruudut_paino = 0.5
        paras_mahd_paino = 0.0

        laudan_arvo = self.laske_laudan_arvo(lauta)
        tyhjat = self.laske_tyhjat(lauta)
        monotoonisuus = self.laske_mono(siirto, lauta)
        kulma_pit = self.laske_kulma_arvo(lauta)
        viereiset = self.laske_vieresiet_ruudut(lauta)
        paras_mahd = self.paras_mahd(lauta)

        return (laudan_arvo * laudan_arvo_paino) + (tyhjat * tyhjat_paino) + (monotoonisuus * mono_paino) + (kulma_pit * kulma_pit_paino) + (viereiset * viereiset_ruudut_paino) + (paras_mahd * paras_mahd_paino)

    def paras_mahd(self, lauta):
        'Paras mahdollinen jono ruutuja'
        '''[[65536,32768,16384,8192]
            [512,1024,2048,4096]
            [256,128,64,32]
            [2,4,8,16]]'''
        arvot = []
        arvo = 0
        for rivi in lauta:
            for i in rivi:
                arvot.append(i)
        arvot.sort(reverse=True)
        if arvot[0] == lauta[0][0] and arvot[0] != 0:
            arvo += 1
        if arvot[1] == lauta[0][1] and arvot[1] != 0:
            arvo += 1
        if arvot[2] == lauta[0][2] and arvot[2] != 0:
            arvo += 1
        if arvot[3] == lauta[0][3] and arvot[3] != 0:
            arvo += 1
        if arvot[4] == lauta[1][3] and arvot[4] != 0:
            arvo += 1
        if arvot[5] == lauta[1][2] and arvot[5] != 0:
            arvo += 1
        if arvot[6] == lauta[1][1] and arvot[6] != 0:
            arvo += 1
        if arvot[7] == lauta[1][0] and arvot[7] != 0:
            arvo += 1
        if arvot[8] == lauta[2][0] and arvot[8] != 0:
            arvo += 1
        if arvot[9] == lauta[2][1] and arvot[9] != 0:
            arvo += 1
        if arvot[10] == lauta[2][2] and arvot[10] != 0:
            arvo += 1
        if arvot[11] == lauta[2][3] and arvot[11] != 0:
            arvo += 1
        if arvot[12] == lauta[3][3] and arvot[12] != 0:
            arvo += 1
        if arvot[13] == lauta[3][2] and arvot[13] != 0:
            arvo += 1
        if arvot[14] == lauta[3][1] and arvot[14] != 0:
            arvo += 1
        if arvot[15] == lauta[3][0] and arvot[15] != 0:
            arvo += 1
        return arvo

    def laske_vieresiet_ruudut(self, lauta):
        'Laskee arvon sen mukaan onko tyhjän ruudun vieressä kaksi samaa arvoa'
        'Auttaa pitämään kentän tyhjänä'
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
        'Laskee manattan pituuden suurimmasta arvosta lähimpään nurkkaan'
        kulmat = [(0, 0), (3, 0), (0, 3), (3, 3)]
        korkein_arvo = 0
        korkein_arvo_paikka = None
        for rivi in range(len(lauta)):
            for sarake in range(len(lauta[0])):
                if lauta[rivi][sarake] > korkein_arvo:
                    korkein_arvo = lauta[rivi][sarake]
                    korkein_arvo_paikka = (rivi, sarake)
        # Laskee manhattan pituudet nurkkiin (jos arvo on nurkassa muutetaan arvo 1 koska muuten jaetaan nollalla)
        pituudet_kulmaan = [abs(korkein_arvo_paikka[0] - kulma[0]) + abs(korkein_arvo_paikka[1] - kulma[1]) if abs(
            korkein_arvo_paikka[0] - kulma[0]) + abs(korkein_arvo_paikka[1] - kulma[1]) != 0 else 1 for kulma in kulmat]
        # Ottaa lyhimmän arvon ja palauttaa sen käänteisluvun
        return 1/min(pituudet_kulmaan)

    def laske_laudan_arvo(self, lauta):
        'Laskee laudan arvon vain sen mukaan kuinka suuret arvot ovat ruudulla'
        arvo = 0
        for y in range(len(lauta)):
            for x in range(len(lauta[0])):

                arvo += lauta[y][x]
        return arvo

    def laske_tyhjat(self, lauta):
        'laskee tyhjien ruutujen määrän'
        tyhjat = 0
        for y in range(len(lauta)):
            for x in range(len(lauta[0])):
                if lauta[y][x] == 0:
                    tyhjat += 1

        return tyhjat

    def laske_mono(self, siirto, lauta):
        'laskee monotoonisuudelle arvon'
        if siirto == 'ylos':
            ruudut = [(0, 0), (0, 1), (0, 2), (0, 3)]
        elif siirto == 'alas':
            ruudut = [(3, 0), (3, 1), (3, 2), (3, 3)]
        elif siirto == 'vasen':
            ruudut = [(0, 0), (1, 0), (2, 0), (3, 0)]
        elif siirto == 'oikea':
            ruudut = [(0, 3), (1, 3), (2, 3), (3, 3)]
        arvo = 0
        for rivi, sarake in ruudut:
            for i in range(1, 4):
                if sarake + i < 4:
                    nykyinen = lauta[rivi][sarake + i - 1]
                    seuraava = lauta[rivi][sarake + i]
                    while seuraava == 0 and i + 1 < 4:
                        i += 1
                        if sarake + i < 4:
                            seuraava = lauta[rivi][sarake + i]
                        else:
                            break

                    if nykyinen <= seuraava:
                        arvo += 1

        return arvo

    def seuraava_siirto(self, lauta = None):
        'hakee seuravaaksi parhaan siirron'
        paras_siirto = ''
        paras_arvo = 0
        for siirto in ['ylos', 'alas', 'vasen', 'oikea']:
            arvo = self.laske_arvot(siirto)
            if arvo > paras_arvo:
                paras_arvo = arvo
                paras_siirto = siirto
        if not lauta:
            
            self.peli = logiikka.lauta()
        else:
            self.peli = lauta
        return paras_siirto

    def laske_arvot(self, siirto):
        'Tekee siirron ja laskee siirron jälkeisen laudan arvon'
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
        return self.luo_arvo(uusi_lauta, 0, self.syvyys, siirto)

    def luo_arvo(self, lauta, nykyinen_syvyys, syvyys_raja, siirto):
        'Lisää 2 ja 4 tyhjiin ruutuihin'
        if nykyinen_syvyys == syvyys_raja:  # Lasketaan siirrolle heuristinen arvo kun syvyysrajaan päästään
            return self.laske_arvo(lauta, siirto)
        arvo = 0
        for y in range(len(lauta)):
            for x in range(len(lauta[0])):
                if lauta[y][x] == 0:
                    # Lisää 2 tyhjään kohtaan
                    uusi_lauta2 = lauta
                    uusi_lauta2[y][x] = 2
                    arvo2 = self.laske_siirron_arvo(
                        uusi_lauta2, nykyinen_syvyys, syvyys_raja)
                    arvo = arvo + (0.9 * arvo2)

                    # Lisää 4 tyhjään kohtaan
                    uusi_lauta4 = lauta
                    uusi_lauta4[y][x] = 4
                    arvo4 = self.laske_siirron_arvo(
                        uusi_lauta4, nykyinen_syvyys, syvyys_raja)
                    arvo = arvo + (0.1*arvo4)
        return arvo

    def laske_siirron_arvo(self, lauta, nykyinen_syvyys, syvyys_raja):
        'Tekee seuraavan siirron kun arvo on lisätty lautaan'
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
                siirron_arvo = self.luo_arvo(
                    uusi_lauta, nykyinen_syvyys+1, syvyys_raja, siirto)
                arvo = max([arvo, siirron_arvo])

        return arvo


ratkoja = Ratkoja()
