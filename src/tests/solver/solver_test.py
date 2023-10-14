import unittest
from solver.game_ai import ratkoja

class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_laske_arvo(self):
        self.assertEqual(8257536, ratkoja.laske_arvo([[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    