import unittest
from solver.game_solver import ratkoja
from solver.expectimax import uusi_node

class TestSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.juuri = uusi_node(0,None)

    def test_laske_arvo(self):
        self.assertEqual(4194320, ratkoja.laske_arvo([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,2,4]]))
    
    def test_tee_nodet(self):
        self.assertEqual(5, ratkoja.tee_nodet(3))