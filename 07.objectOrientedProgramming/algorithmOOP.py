"""
@author: Fábio Mori
"""

#Escola Matriz - Class 19: Object Oriented Programming
#Correct code with OOP

class jogos:
    def __init__(self, nome, ano, tipo, video_game, valor):
        self.nome=nome
        self.ano=ano
        self.tipo=tipo
        self.video_game=video_game
        self.valor=valor
            
    def imprimir(self):
        print('\nO jogo foi lançado em', self.ano, 
              '\nÉ‰ do tipo', self.tipo,
              '\nPara jogar no ví­deo game', self.video_game,
              '\nE custa um valor de R$', self.valor)

jogo1=jogos('The Legend of Zelda', 1998, 'Aventura', 'Nintendo 64', 350)
jogo2=jogos('Mario Kart 64', 1996, 'Corrida', 'Nintendo 64', 300)
jogo3=jogos('Banjo Kazooie', 1998, 'Aventura', 'Nintendo 64', 300)
jogo4=jogos('Sonic', 1991, 'Aventura', 'Mega Drive', 250)
jogo5=jogos('Super Mario World', 1992, 'Aventura', 'Super Nintendo', 200)
jogo6=jogos('O Rei Leão', 1994, 'Aventura', 'Super Nintendo', 200)

jogo=input('Digite o nome do jogo: ')

if jogo == jogo1.nome:
    jogo1.imprimir()
elif jogo == jogo2.nome:
    jogo2.imprimir()
elif jogo == jogo3.nome:
    jogo3.imprimir()
elif jogo == jogo4.nome:
    jogo4.imprimir()
elif jogo == jogo5.nome:
    jogo5.imprimir()
elif jogo == jogo6.nome:
    jogo6.imprimir()
else:
    print('Não temos este jogo')


 