import unittest
import random
from tempo import Tempo

t = random.randint(-20,49)

class TestTempo(unittest.TestCase):

    
    def setUp(self):
        self.tempo1 = Tempo(t)
        self.tempo2 = Tempo(t)
        self.tempo3 = Tempo(t)

        self.tempo_a = Tempo(3)
        self.tempo_b = Tempo(15)
        self.tempo_c = Tempo(32)

    #Testar com os tempos se eles devolvem True ou False nas seguintes funções:
    def test_esta_quente(self):
        return

    def test_esta_frio(self):
        return

    def test_esta_morno(self):
        return
    
    #Testar com os tempos se eles devolvem int ou float nas seguintes funções:
    def test_fahrenheit(self):
        return

    def test_kelvin(self):
        return

if __name__ == '__main__':
    unittest.main()