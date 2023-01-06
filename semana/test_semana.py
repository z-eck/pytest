import unittest
from semana import *

class TestSemana(unittest.TestCase):

    def test_dia_da_semana(self):
        self.assertTrue(dia_da_semana(2,20))
        self.assertFalse(dia_da_semana(5,20))
    
    def test_final_de_semana(self):
        self.assertFalse(final_de_semana(2,20))
        self.assertTrue(final_de_semana(5,20))


if __name__ == '__main__':
    unittest.main()