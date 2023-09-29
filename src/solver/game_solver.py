from solver.expectimax import uusi_node, expectimax
from game.game_logic import logiikka

PARAS_TILANNE = [[2**16,2**15,2**13,2**11],
                 [2**14,2**9,2**8,2**6],
                 [2**12,2**7,2**4,2**3],
                 [2**10,2**5,2**2,2]] #Tällä lasketaan laudan arvot

class Ratkoja:
    'Tähän tulee itse pelin ratkaisija. '
    def __init__(self):
        'Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden'
        self.juuri = uusi_node(0, None)
        self.depth = 8
        self.aloita_alusta()

    def laske_arvo(self, lauta):
        'Laskee kentän arvon joka myöhemmin toimii noden arvona'
        'Heurestiikka on vielä kehitteillä'
        arvo = 0
        maximum = max([max(i) for i in lauta])
        if logiikka.get_current_state(lauta=lauta) == 'Hävisit pelin!':
            arvo = 0
        elif logiikka.get_current_state(lauta=lauta) == 'Sinä voitit!':
            arvo = 99999999999999999999999999
        else:
            for i in range(len(self.peli)):
                for j in range(len(self.peli[0])):
                    arvo += lauta[i][j] * PARAS_TILANNE[i][j]
            #for i in range(len(self.peli)):
            #    for j in range(len(self.peli[0])):
            #        if lauta[i][j] == 0:
            #            arvo += 1
                
        return arvo
    
    def aloita_alusta(self):
        'Nollaa juuri noden'
        self.peli = logiikka.lauta()

        self.juuri.alas = None
        self.juuri.ylos = None
        self.juuri.oikea = None
        self.juuri.vasen = None

    def tee_nodet(self, syvyys = None):
        'Tekee hakupuun kaikki nodet'
        maara = 0
        for i in range(1,self.depth+1 if not syvyys else syvyys):
            if i == 1:
                pelit = [self.peli]
                vanhemmat = [self.juuri]

            if i != 1:
                pelit = pelit[4**(i-2):]
                vanhemmat = vanhemmat[4**(i-2):]
            
            maara += len(vanhemmat)
            for j in range(0,4**(i-1)):
                muuttunut1, oikea = logiikka.oikea(pelit[j])
                muuttunut2, vasen = logiikka.vasen(pelit[j])
                muuttunut3, ylos = logiikka.ylos(pelit[j])
                muuttunut4, alas = logiikka.alas(pelit[j])

                if muuttunut1 and vanhemmat[j] != None:
                    vanhemmat[j].oikea = uusi_node(self.laske_arvo(oikea), vanhemmat[j])
                if muuttunut2 and vanhemmat[j] != None:
                    vanhemmat[j].vasen = uusi_node(self.laske_arvo(vasen), vanhemmat[j])
                if muuttunut3 and vanhemmat[j] != None:
                    vanhemmat[j].ylos = uusi_node(self.laske_arvo(ylos),vanhemmat[j])
                if muuttunut4 and vanhemmat[j] != None:
                    vanhemmat[j].alas = uusi_node(self.laske_arvo(alas), vanhemmat[j])

                vanhemmat.append(vanhemmat[j].oikea if vanhemmat[j] != None else None)
                vanhemmat.append(vanhemmat[j].vasen if vanhemmat[j] != None else None)
                vanhemmat.append(vanhemmat[j].ylos if vanhemmat[j] != None else None)
                vanhemmat.append(vanhemmat[j].alas if vanhemmat[j] != None else None)

                pelit.append(oikea)
                pelit.append(vasen)
                pelit.append(ylos)
                pelit.append(alas)
        return maara

    def seuraava_siirto(self):
        'Tekee siirron ja päivittää näytön jotta käyttäjä näkee siirron'
        siirto = expectimax(self.juuri, True)
        print(siirto)

        return siirto[1][0]
    
ratkoja = Ratkoja()