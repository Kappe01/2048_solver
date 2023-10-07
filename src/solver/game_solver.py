from solver.expectimax import Node, expectimax
from game.game_logic import logiikka

PARAS_TILANNE = [[2**16,2**15,2**14,2**13],
                 [2**9,2**10,2**11,2**12],
                 [2**8,2**7,2**6,2**5],
                 [2**1,2**2,2**3,2**4]] #Tällä lasketaan laudan arvot

class Ratkoja:
    'Tähän tulee itse pelin ratkaisija. '
    def __init__(self):
        'Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden'
        self.juuri = Node(0, None)
        self.depth = 3
        self.aloita_alusta()

    def laske_arvo(self, lauta):
        'Laskee kentän arvon joka myöhemmin toimii noden arvona'
        'Heurestiikka on vielä kehitteillä'
        arvo = 0
        tyhjat = 0
        maksimi = 0
        maksimi_oikea = 0
        maksimi_loyto = 0
        arvot = []
        for i in range(len(self.peli)):
            if max(self.peli[i]) > maksimi_oikea:
                maksimi_oikea = max(self.peli[i])
            if max(lauta[i]) > maksimi:
                maksimi = max(lauta[i])
            for j in range(len(self.peli[0])):
                if lauta[i][j] not in arvot:
                    arvot.append(lauta[i][j])
        arvot.sort()
        if maksimi > maksimi_oikea: 
            arvo *= 10**3
        for i in range(len(self.peli)):
            for j in range(len(self.peli[0])):
                if lauta[i][j] == 0:
                    tyhjat += 1
                if i == 0:
                    if len(arvot) >= 4:
                        if lauta[i][j] in arvot[-4:]:
                            arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                        else:
                            arvo += lauta[i][j]
                    else:
                        arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                    if lauta[i][j] == maksimi and maksimi_loyto == 0:
                        maksimi_loyto = 1
                        arvo *= 4
                if len(arvot) >= 4:
                    if i == 1:
                        if len(arvot) >= 8:
                            if lauta[i][j] in arvot[-8:-4]:
                                arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                            else:
                                arvo += lauta[i][j]
                        else:
                            arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                    if len(arvot) >= 8:
                        if i == 2:
                            if len(arvot) >= 12:
                                if lauta[i][j] in arvot[-12:-8]:
                                    arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                                else:
                                    arvo += lauta[i][j]
                            else:
                                arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                        if len(arvot) >= 12:
                            if i == 3:
                                if len(arvot) >= 16:
                                    if lauta[i][j] in arvot[-16:-12]:
                                        arvo += lauta[i][j] * PARAS_TILANNE[i][j]
                                    else:
                                        arvo += lauta[i][j]
                                else:
                                    arvo += lauta[i][j] * PARAS_TILANNE[i][j]
        return arvo*tyhjat
    
    def aloita_alusta(self):
        'Nollaa juuri noden'
        self.peli = logiikka.lauta()

        self.juuri.poista_lapset()

    def tee_nodet(self, syvyys = None):
        'Tekee hakupuun kaikki nodet'
        maara = 0
        vanha = 0
        for i in range(1,self.depth+1 if not syvyys else syvyys):
            if i == 1:
                pelit = [self.peli]
                vanhemmat = [self.juuri]

            if i != 1:
                pelit = pelit[vanha:]
                vanhemmat = vanhemmat[vanha:]
            
            maara += len(vanhemmat)
            vanha = len(vanhemmat)

            for j in range(len(vanhemmat)):
                if vanhemmat[j] is None:
                    continue

                muuttunut1, oikea = logiikka.oikea(pelit[j])
                muuttunut2, vasen = logiikka.vasen(pelit[j])
                muuttunut3, ylos = logiikka.ylos(pelit[j])
                muuttunut4, alas = logiikka.alas(pelit[j])

                if muuttunut1 and vanhemmat[j] != None:
                    for a in range(len(oikea)):
                        for k in range(len(oikea[0])):
                            oikea_temp = [rivi[:] for rivi in oikea]
                            if oikea[a][k] == 0:
                                oikea_temp[a][k] = 2
                                pelit.append(oikea_temp)
                                vanhemmat[j].lisaa_lapsi('oikea', Node(self.laske_arvo(oikea_temp), vanhemmat[j]))
                if muuttunut2 and vanhemmat[j] != None:
                    for a in range(len(oikea)):
                        for k in range(len(oikea[0])):
                            vasen_temp = [rivi[:] for rivi in vasen]
                            if vasen[a][k] == 0:
                                vasen_temp[a][k] = 2
                                pelit.append(vasen_temp)
                                vanhemmat[j].lisaa_lapsi('vasen', Node(self.laske_arvo(vasen_temp), vanhemmat[j]))
                if muuttunut3 and vanhemmat[j] != None:
                    for a in range(len(oikea)):
                        for k in range(len(oikea[0])):
                            ylos_temp = [rivi[:] for rivi in ylos]
                            if ylos[a][k] == 0:
                                ylos_temp[a][k] = 2
                                pelit.append(ylos_temp)
                                vanhemmat[j].lisaa_lapsi('ylos', Node(self.laske_arvo(ylos_temp), vanhemmat[j]))
                if muuttunut4 and vanhemmat[j] != None:
                    for a in range(len(oikea)):
                        for k in range(len(oikea[0])):
                            alas_temp = [rivi[:] for rivi in alas]
                            if alas[a][k] == 0:
                                alas_temp[a][k] = 2
                                pelit.append(alas_temp)
                                vanhemmat[j].lisaa_lapsi('alas', Node(self.laske_arvo(alas_temp), vanhemmat[j]))

                vasemmat_lapset = vanhemmat[j].hae_lapsi('vasen')
                oikea_laspet = vanhemmat[j].hae_lapsi('oikea')
                yla_lapset = vanhemmat[j].hae_lapsi('ylos')
                ala_laspet = vanhemmat[j].hae_lapsi('alas')
                for lapsi in vasemmat_lapset:
                    vanhemmat.append(lapsi)
                for lapsi in oikea_laspet:
                    vanhemmat.append(lapsi)
                for lapsi in yla_lapset:
                    vanhemmat.append(lapsi)
                for lapsi in ala_laspet:
                    vanhemmat.append(lapsi)

        return maara

    def seuraava_siirto(self):
        'Tekee siirron ja päivittää näytön jotta käyttäjä näkee siirron'
        arvo, polku = expectimax(self.juuri, True)
        print(arvo, polku)

        return polku[0]
    
ratkoja = Ratkoja()