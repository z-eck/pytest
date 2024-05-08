import unittest
from portaria import portaria

class TestPortaria(unittest.TestCase):

    #Faça um teste para dar negado na idade, negado no tipo de convite, negado no código e um sucesso com bem-vindo
    def test_portaria(self):
        self.assertEqual(portaria(0, "", ""), "Negado.") #idade
        self.assertEqual(portaria(0, "", ""), "Negado.") #tipo_convite
        self.assertEqual(portaria(0, "", ""), "Negado.") #codigo
        self.assertEqual(portaria(0, "", ""), "Bem-vindo!") #sucesso


if __name__ == '__main__':
    unittest.main()