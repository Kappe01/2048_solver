class Node:
    '''Nodejen luokka
    Nodet saavat jonkun arvon joka mallintaa nykyistä peli tilannetta

    Tällähetkellä kaikista nodeista lähtee 4 polkua.
    Tätä voisi mahdollisesti laajentaa niin että on kaikki eri mahdollisuudet mihin 2 tai 4 voi mennä.
    Eli laajentaa noin 40 polkuun. 
    '''

    def __init__(self, arvo, vanhempi):
        self.arvo = arvo
        self.vasen = None
        self.oikea = None
        self.ylos = None
        self.alas = None
        self.vanhempi = vanhempi


def uusi_node(arvo, vanhempi):
    'Luo uuden noden'
    temp = Node(arvo, vanhempi)

    return temp


def expectimax(node, vuoro, seuraava=None, polku=[]):
    if seuraava is None:
        seuraava = ''

    if node is None:
        return None

    if node.vasen is None and node.oikea is None and node.ylos is None and node.alas is None:
        return node.arvo, polku

    if vuoro:
        siirrot = [('vasen', node.vasen), ('oikea', node.oikea),
                   ('ylos', node.ylos), ('alas', node.alas)]
        max_arvo = float('-inf')
        paras_siirto = ''
        for siirto, lapsi in siirrot:
            if lapsi is not None:
                uusi_siirto = siirto
                arvo, lapsen_polku = expectimax(lapsi, False, uusi_siirto, polku + [uusi_siirto])
                if arvo > max_arvo:
                    max_arvo = arvo
                    paras_siirto = uusi_siirto

        return max_arvo, polku + [paras_siirto]

    lapset = [node.vasen, node.oikea, node.ylos, node.alas]
    lapset_ei_none = [lapsi for lapsi in lapset if lapsi is not None]
    
    if lapset_ei_none:
        keskiarvo = sum(expectimax(lapsi, True, seuraava, polku)[0] for lapsi in lapset_ei_none) / len(lapset_ei_none)
        return keskiarvo, polku
    else:
        return 0, polku
    