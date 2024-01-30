import unittest
from solver.expectimax import Node, expectimax, hae_siirto


class TestYourFile(unittest.TestCase):
    def setUp(self) -> None:
        self.lauta = [[2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def test_on_terminal(self):
        valmis_lauta = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [512, 1024, 2048, 4096],
            [8192, 16384, 32768, 65536],
        ]

        valmis_node = Node(valmis_lauta)
        ei_valmis_node = Node(self.lauta)

        self.assertTrue(valmis_node.on_terminal())
        self.assertFalse(ei_valmis_node.on_terminal())

    def test_expectimax(self):
        node = Node(self.lauta)
        result = expectimax(node, 3, True)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, (int, float))

    def test_hae_siirto(self):
        alku_node = Node(self.lauta)
        result = hae_siirto(alku_node)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertIn(result, ["ylos", "alas", "vasen", "oikea"])
