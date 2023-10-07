class Node:
    '''Nodejen luokka
    Nodet saavat jonkun arvon joka mallintaa nykyistä peli tilannetta

    Tällähetkellä kaikista nodeista lähtee 4 polkua.
    Tätä voisi mahdollisesti laajentaa niin että on kaikki eri mahdollisuudet mihin 2 tai 4 voi mennä.
    Eli laajentaa noin 40 polkuun. 
    '''

    def __init__(self, arvo, vanhempi):
        self.arvo = arvo
        self.lapset = {}
        self.vanhempi = vanhempi
    
    def lisaa_lapsi(self, siirto, node):
        if siirto not in self.lapset:
            self.lapset[siirto] = []
        self.lapset[siirto].append(node)

    def hae_lapsi(self, siirto):
        return self.lapset.get(siirto, [])

    def poista_lapset(self):
        self.lapset = {}

def expectimax(node, vuoro, seuraava=None, polku=[]):
    if seuraava is None:
        seuraava = ''

    if node is None:
        return None

    if len(node.hae_lapsi('oikea')) == 0 and len(node.hae_lapsi('vasen')) == 0 and len(node.hae_lapsi('ylos')) == 0 and len(node.hae_lapsi('alas')) == 0:
        return node.arvo, polku

    max_arvo = float('-inf')
    paras_siirrot = []
    paras_polku = []

    if vuoro:
        siirrot = [('vasen', node.hae_lapsi('vasen')), ('oikea', node.hae_lapsi('oikea')),
                   ('ylos', node.hae_lapsi('ylos')), ('alas', node.hae_lapsi('alas'))]

        for siirto, lapset in siirrot:
            for lapsi in lapset:
                if lapsi is not None:
                    uusi_siirto = siirto
                    arvo, lapsen_polku = expectimax(lapsi, False, uusi_siirto, polku + [uusi_siirto])
                    if arvo > max_arvo:
                        max_arvo = arvo
                        paras_siirrot = [uusi_siirto]
                        paras_polku = lapsen_polku
                    elif arvo == max_arvo:
                        paras_siirrot.append(uusi_siirto)
        if max_arvo == float('-inf'):
            return node.arvo, polku

        return max_arvo, paras_siirrot + paras_polku

    lapset = [node.hae_lapsi('vasen'), node.hae_lapsi('oikea'), node.hae_lapsi('ylos'), node.hae_lapsi('alas')]
    paras_polku = []

    for lapsi in lapset:
        lapset_ei_none = [i for i in lapsi if i is not None]

    if not lapset_ei_none:
        return node.arvo, polku

    for lapsi in lapset_ei_none:
        keskiarvo = sum(expectimax(lapsi, True, seuraava, polku)[0] for lapsi in lapset_ei_none) / len(lapset_ei_none)
        if keskiarvo > max_arvo:
            max_arvo = keskiarvo
            paras_polku = expectimax(lapsi, True, seuraava, polku)[1]

    return max_arvo, paras_polku
