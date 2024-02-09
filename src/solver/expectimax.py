import math
from solver.herustics import Ratkoja
from game.game_logic import logiikka


class Node:
    def __init__(self, lauta):
        self.lauta = lauta

    def on_terminal(self):
        tulos = logiikka.hae_nykyinen_tila(self.lauta)

        if tulos == "Hävisit pelin!":
            return True
        return False

    def hae_lapset(self):
        lapset = []
        for siirto in ["ylos", "alas", "vasen", "oikea"]:
            if siirto == "ylos":
                muuttunut, lapsi_lauta = logiikka.ylos(self.lauta)
                nykyinen_siirto = "ylos"
            elif siirto == "alas":
                muuttunut, lapsi_lauta = logiikka.alas(self.lauta)
                nykyinen_siirto = "alas"
            elif siirto == "vasen":
                muuttunut, lapsi_lauta = logiikka.vasen(self.lauta)
                nykyinen_siirto = "vasen"
            elif siirto == "oikea":
                muuttunut, lapsi_lauta = logiikka.oikea(self.lauta)
                nykyinen_siirto = "oikea"

            if muuttunut:
                lapset.append((Node(lapsi_lauta), nykyinen_siirto))

        return lapset

    def hae_lapset_todennakoisyyksineen(self):
        lapset = []

        for y in range(4):
            for x in range(4):
                lapsi_lauta_2 = [row.copy() for row in self.lauta]
                lapsi_lauta_4 = [row.copy() for row in self.lauta]

                if self.lauta[y][x] == 0:
                    lapsi_lauta_2[y][x] = 2
                    lapsi_lauta_4[y][x] = 4

                    lapset.append((Node(lapsi_lauta_2), 0.9))
                    lapset.append((Node(lapsi_lauta_4), 0.1))
        return lapset


def expectimax(node: Node, syvyys: int, pelaajan_vuoro: bool):
    if syvyys == 0 or node.on_terminal():
        return Ratkoja(node.lauta).laske_arvo()

    if pelaajan_vuoro:
        alpha = -math.inf
        lapset = node.hae_lapset()
        for lapsi, siirto in lapset:
            alpha = max(alpha, expectimax(lapsi, syvyys - 1, False))

    else:
        alpha = 0
        for lapsi, todennakoisyys in node.hae_lapset_todennakoisyyksineen():
            alpha += todennakoisyys * expectimax(lapsi, syvyys - 1, True)

    return alpha


def hae_siirto(alku_node: Node):
    alpha = -math.inf
    syvyys = 4
    tyhjat = 0
    paras_siirto = None
    for y in range(4):
        for x in range(4):
            if alku_node.lauta[y][x] == 0:
                tyhjat += 1
    if tyhjat < 6:
        syvyys = 5
    if tyhjat < 4:
        syvyys = 6
    lapset = alku_node.hae_lapset()
    for lapsi, siirto in lapset:
        new_alpha = expectimax(lapsi, syvyys, False)
        print(new_alpha, alpha)
        if new_alpha > alpha:
            alpha = new_alpha
            paras_siirto = siirto

    return paras_siirto
