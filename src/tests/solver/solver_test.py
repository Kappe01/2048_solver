import unittest
from solver.game_solver import ratkoja

class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_laske_arvo(self):
        self.assertEqual(8257536, ratkoja.laske_arvo([[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    
    def test_tee_nodet(self):
        self.assertLess(30, ratkoja.tee_nodet(3))