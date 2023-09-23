from solver.expectimax import uusi_node, expectimax
from game.game_logic import logiikka
from game.game_ui import aloita

PARAS_TILANNE = [[2**16,2**15,2**14,2**13],
                 [2**9,2**10,2**11,2**12],
                 [2**8,2**7,2**6,2**5],
                 [2,2**2,2**3,2**4]] #Tällä lasketaan laudan arvot

class Ratkoja:
    'Tähän tulee itse pelin ratkaisija. '
    'Ei ole vielä suoritettavissa'
    def __init__(self):
        'Hakee nykyisen peli tilanteen ja tekee ensimmäisen noden'
        self.peli = logiikka.lauta()
        self.juuri = uusi_node(0)

    def laske_arvo(self, lauta):
        'Laskee kentän arvon joka myöhemmin toimii noden arvona'
        arvo = 0
        for i in range(len(self.peli)):
            for j in range(len(self.peli[0])):
                arvo += lauta[i][j] * PARAS_TILANNE[i][j]
        return arvo
    
    def aloita_alusta(self):
        'Nollaa juuri noden'
        self.juuri.alas = None
        self.juuri.ylos = None
        self.juuri.oikea = None
        self.juuri.vasen = None

    def tee_node(self, node, arvo):
        node = uusi_node(arvo)

    def seuraava_siirto(self):
        'Tekee siirron ja päivittää näytön jotta käyttäjä näkee siirron'
        siirto = expectimax(self.juuri, True)

        if siirto == 'vasen':
            logiikka.vasen()
        elif siirto == 'oikea':
            logiikka.oikea()
        elif siirto == 'ylos':
            logiikka.ylos()
        elif siirto == 'alas':
            logiikka.alas()
        
        aloita.paivita()
        self.peli = logiikka.lauta()