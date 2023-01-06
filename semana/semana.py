dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

def dia_da_semana(dia, hora):
    if dia >= 7 or dia <= -1:
        print("Este dia da semana não existe! Escolha um de 0 à 6!")
        return False
    if hora >= 24 or hora <= -1:
        print("Esta hora é além do tempo! Escolha uma existente entre 0 à 23!")
        return False
    if dias[dia] == "sábado" or dias[dia] == "domingo" or (hora >= 18 and dias[dia] == "sexta-feira"):
        print("Não é um dia da semana!")
        return False
    else:
        print("É um dia da semana! :D")
        return True

def final_de_semana(dia,hora):
    if dia != int or hora != int:
        print("Somente números inteiros!")
        return False
    if dia >= 7 or dia <= -1:
        print("Este dia da semana não existe! Escolha um de 0 à 6!")
        return False
    if hora >= 24 or hora <= -1:
        print("Esta hora é além do tempo! Escolha uma existente entre 0 à 23!")
        return False
    if dias[dia] == "sábado" or dias[dia] == "domingo" or (hora >= 18 and dias[dia] == "sexta-feira"):
        print ("É um dia de final de semana!")
        return True
    else:
        print("Não é um dia de final de semana!")
        return False

#dia_da_semana(4,20)