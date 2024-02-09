import unittest

from game.game_logic import Logic


class TestLogic(unittest.TestCase):
    def setUp(self) -> None:
        self.start = Logic()

    def test_laudan_alustus(self):
        arvot = 0
        lauta = Logic.lauta(self.start)
        for i in range(len(lauta)):
            for j in range(len(lauta[i])):
                if lauta[i][j] == 2 or lauta[i][j] == 4:
                    arvot += 1

        self.assertEqual(arvot, 2)

    def test_arvon_lisays(self):
        arvot = 0
        Logic.lisaa_arvo(self.start)
        lauta = Logic.lauta(self.start)
        for i in range(len(lauta)):
            for j in range(len(lauta[i])):
                if lauta[i][j] == 2 or lauta[i][j] == 4:
                    arvot += 1

        self.assertEqual(arvot, 3)

    def test_hae_nykyinen_tila_havio(self):
        lauta = [[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]
        tulos = Logic.hae_nykyinen_tila(self.start, lauta=lauta)

        self.assertEqual(tulos, "Hävisit pelin!")

    def test_tiivistys(self):
        arvot = 0
        muuttunut, lauta = Logic.tiivista(self.start, self.start.peli_lauta)

        for i in range(len(lauta)):
            for j in range(1):
                if lauta[i][j] == 2 or lauta[i][j] == 4:
                    arvot += 1

        self.assertTrue(arvot >= 1)

    def test_yhdista(self):
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        # Lisätään 8 arvoa niin jollain rivillä on vähintään 2 arvoa
        Logic.lisaa_arvo(self.start)
        Logic.tiivista(self.start, self.start.peli_lauta)
        # Jos palauttaa true on jotkut arvot yhdistynyt
        muuttunut, lauta = Logic.yhdista(self.start, self.start.peli_lauta)

        self.assertTrue(muuttunut == True)

    def test_ylos(self):
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.tiivista(self.start, self.start.peli_lauta)
        muuttunut, lauta = Logic.ylos(self.start)

        self.assertTrue(muuttunut == True)

    def test_alas(self):
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.tiivista(self.start, self.start.peli_lauta)
        muuttunut, lauta = Logic.alas(self.start)

        self.assertTrue(muuttunut == True)

    def test_oikea(self):
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.tiivista(self.start, self.start.peli_lauta)
        muuttunut, lauta = Logic.oikea(self.start)

        self.assertTrue(muuttunut == True)

    def test_vasen(self):
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.lisaa_arvo(self.start)
        Logic.tiivista(self.start, self.start.peli_lauta)
        muuttunut, lauta = Logic.vasen(self.start)

        self.assertTrue(muuttunut == True)
