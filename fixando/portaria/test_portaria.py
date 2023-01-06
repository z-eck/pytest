import unittest
from portaria import portaria

class TestPortaria(unittest.TestCase):

    #Faça um teste para dar negado na idade, negado no tipo de convite, negado no código e um sucesso com bem-vindo
    def test_portaria(self):
        self.assertEqual(portaria(0, "", ""), "Negado.")
        self.assertEqual(portaria(0, "", ""), "Negado.")
        self.assertEqual(portaria(0, "", ""), "Negado.")
        self.assertEqual(portaria(0, "", ""), "Bem-vindo!")


if __name__ == '__main__':
    unittest.main()