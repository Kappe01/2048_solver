import unittest

import solver.expectimax as Exp


class TestExpectimax(unittest.TestCase):
    def test_uusi_node(self):
        test = Exp.uusi_node(10, None)
        self.assertEqual(test.arvo, 10)

    def test_expectimax(self):
        juuri = Exp.uusi_node(10,None)
        juuri.alas = Exp.uusi_node(20,juuri)
        juuri.ylos = Exp.uusi_node(30,juuri)
        juuri.alas.alas = Exp.uusi_node(100,juuri.alas)
        juuri.ylos.oikea = Exp.uusi_node(200,juuri.ylos)
        juuri.vasen = Exp.uusi_node(500,juuri)

        siirto = Exp.expectimax(juuri, True)

        self.assertEqual(siirto, ['vasen',[]])
