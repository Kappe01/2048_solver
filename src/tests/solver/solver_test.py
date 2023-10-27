import unittest
from solver.game_ai import ratkoja


class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.lauta = [[2,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]

    def test_aseta_syvyys(self):
        self.assertEqual(2, ratkoja.aseta_syvyys(2))

    def test_paras_mahd(self):
        self.assertEqual(1, ratkoja.paras_mahd(self.lauta))
        
    def test_laske_viereiset(self):
        self.assertEqual(25, ratkoja.laske_vieresiet_ruudut([[0,2,2,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    
    def test_laske_kulma(self):
        self.assertEqual(1, ratkoja.laske_kulma_arvo(self.lauta))

    def test_laske_laudan_arvo(self):
        self.assertEqual(2, ratkoja.laske_laudan_arvo(self.lauta))

    def test_laske_tyhjat(self):
        self.assertEqual(15, ratkoja.laske_tyhjat(self.lauta))
    
    def test_laske_arvo(self):
        self.assertEqual(19.1, ratkoja.laske_arvo(self.lauta, 'vasen'))
    
    def test_siirron_haku(self):
        self.assertIsNotNone('alas', ratkoja.seuraava_siirto(self.lauta))