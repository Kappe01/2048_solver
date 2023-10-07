import unittest

import solver.expectimax as Exp


class TestExpectimax(unittest.TestCase):
    def test_uusi_node(self):
        test = Exp.Node(0,None)
        self.assertEqual(test.arvo, 0)

    def test_expectimax(self):
        juuri = Exp.Node(0,None)
        juuri.lisaa_lapsi('vasen', Exp.Node(10,juuri))
        juuri.lisaa_lapsi('ylos',Exp.Node(20, juuri))
        lapset_vasen = juuri.hae_lapsi('vasen')
        lapset_ylos = juuri.hae_lapsi('ylos')
        for lapsi in lapset_vasen:
            lapsi.lisaa_lapsi('alas', Exp.Node(100, lapsi))
        for lapsi in lapset_ylos:
            lapsi.lisaa_lapsi('oikea', Exp.Node(200,lapsi))

        siirto = Exp.expectimax(juuri, True)

        self.assertEqual(siirto, (200, ['ylos', 'oikea']))
