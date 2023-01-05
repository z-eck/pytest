import unittest

class TestClass(unittest.TestCase):

    def teste_meu_metodo(self):
        self.assertEqual(valor_esperado, valor_real, "Mensagem caso o teste falhe")
    
    if __name__ == "__main__":
        unittest.main()