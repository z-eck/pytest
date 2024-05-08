class Campeonato:
    def __init__(self, nome, sobrenome, nick, classe, modo, kills, death, assistance):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nick = nick
        self.classe = classe
        self.modo = modo
        self.kills = kills
        self.death = death
        self.assistance = assistance

    def apresentacao(self):
        return "Eu sou o " + self.nome + " " + self.sobrenome + ", meu nick é " + self.nick + ", eu utilizo a classe de " + self.classe + ", e meu modo favorito é " + self.modo

    def kda(self):
        return (self.kills + self.assistance) / self.death

jogador_ze = Campeonato("Ze", "Costa", "Zezao", "Dano", "CTA", 255, 68, 2)
jogador_luc = Campeonato("Lucas", "Aleixo", "Alexinho", "Tank", "Control", 1, 19, 249)
jogador_senai = Campeonato("Jose", "Senai", "Senai", "Dano", "Outro", 3, 1, 7)

#print(jogador_novo.apresentacao())