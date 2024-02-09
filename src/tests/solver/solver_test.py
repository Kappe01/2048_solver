import unittest
from solver.herustics import Ratkoja


class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.lauta = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.ratkoja = Ratkoja(self.lauta)

    def test_laske_viereiset(self):
        self.assertEqual(
            25,
            self.ratkoja.laske_vieresiet_ruudut(
                [[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            ),
        )

    def test_laske_kulma(self):
        self.assertEqual(1, self.ratkoja.laske_kulma_arvo(self.lauta))

    def test_laske_tyhjat(self):
        self.assertEqual(15, self.ratkoja.laske_tyhjat(self.lauta))

    def test_laske_arvo(self):
        self.assertEqual(64, self.ratkoja.laske_arvo())

    def test_laske_mono(self):
        self.assertEqual(4, self.ratkoja.laske_mono(self.lauta))
