import unittest
from faker import Faker
from campeonato import Campeonato
from mock.mock import *
import random

fake = Faker(['pt-BR'])
nick = Faker()

m = random.randint(0,2)
n = random.randint(0,7)
x = random.randint(0,2000)
y = random.randint(0,500)
z = random.randint(0,2000)

class TestCampeonato(unittest.TestCase):
    def setUp(self):
        self.jogador1 = Campeonato(fake.first_name(), fake.last_name(), nick.last_name(), classe[m], modos[n], x, y, z)
        self.jogador2 = Campeonato(fake.first_name(), fake.last_name(), nick.last_name(), classe[m], modos[n], x, y, z)
        self.jogador3 = Campeonato(fake.first_name(), fake.last_name(), nick.last_name(), classe[m], modos[n], x, y, z)

    def test_apresentacao(self):
        self.assertIs(type(self.jogador1.apresentacao()), str)
        self.assertIs(type(self.jogador2.apresentacao()), str)
    
    def test_kda(self):
        self.assertIs(type(self.jogador2.kda()), float or int)
        self.assertIs(type(self.jogador3.kda()), float or int)

if __name__ == "__main__":
    unittest.main()