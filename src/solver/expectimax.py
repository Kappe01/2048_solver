class Node:
    '''Nodejen luokka
    Nodet saavat jonkun arvon joka mallintaa nykyistä peli tilannetta

    Tällähetkellä kaikista nodeista lähtee 4 polkua.
    Tätä voisi mahdollisesti laajentaa niin että on kaikki eri mahdollisuudet mihin 2 tai 4 voi mennä.
    Eli laajentaa noin 40 polkuun. 
    '''

    def __init__(self, arvo):
        self.arvo = arvo
        self.vasen = None
        self.oikea = None
        self.ylos = None
        self.alas = None


def uusi_node(arvo):
    'Luo uuden noden'
    temp = Node(arvo)

    return temp


def expectimax(node, vuoro, seuraava=None):
    'Hakee algoritmin avulla seuraavan siirron'
    if seuraava is None:
        seuraava = ''

    if node is None:
        return None

    if node.vasen is None and node.oikea is None and node.ylos is None and node.alas is None:
        return node.arvo

    if vuoro:
        siirrot = [('vasen', node.vasen), ('oikea', node.oikea),
                   ('ylos', node.ylos), ('alas', node.alas)]
        max_arvo = float('-inf')
        paras_siirto = None
        for siirto, lapsi in siirrot:
            if lapsi is not None:
                uusi_siirto = siirto
                arvo = expectimax(lapsi, False, uusi_siirto)
                if arvo > max_arvo:
                    max_arvo = arvo
                    paras_siirto = uusi_siirto
        return paras_siirto

    lapset = [node.vasen, node.oikea, node.ylos, node.alas]
    lapset_ei_none = [lapsi for lapsi in lapset if lapsi is not None]
    keskiarvo = sum(expectimax(lapsi, True, seuraava)
                    for lapsi in lapset_ei_none) / len(lapset_ei_none) if lapset_ei_none else 0
    return keskiarvo
