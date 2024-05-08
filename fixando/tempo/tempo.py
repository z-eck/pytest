class Tempo:
    def __init__(self, temperatura):
        self.temperatura = temperatura

        def esta_quente(self):
            if temperatura != int or float:
                return Exception
            if self.temperatura <= 20:
                return False
            else:
                return True
        
        def esta_frio(self):
            if temperatura != int or float:
                return Exception
            if self.temperatura <= 13:
                return True
            else:
                return False
        
        def esta_morno(self):
            if temperatura != int or float:
                return Exception
            if self.temperatura <= 13:
                return False
            elif self.temperatura >= 21:
                return False
            else:
                return True
        
        def fahrenheit(self):
            if temperatura != int or float:
                return Exception
            return (temperatura * 1.8) + 32

        def kelvin(self):
            if temperatura != int or float:
                return Exception
            return temperatura + 273.15