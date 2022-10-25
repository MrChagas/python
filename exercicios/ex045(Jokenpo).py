from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(0.5)
print('=-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*11)
if computador == 0: #CPU PEDRA
    if jogador == 0: #JOGADOR PEDRA
        print('EMPATE')
    elif jogador ==1: #JOGADOR PAPEL
        print('JOGADOR VENCEU')
    elif jogador ==2: #JOGADOR TESOURA
        print('COMPUTADOR VENCEU')
elif computador == 1: #CPU PAPEL
    if jogador == 0: #JOGADOR PEDRA
        print('COMPUTADOR VENCEU')
    elif jogador == 1: #JOGADOR PAPEL
        print('EMPATE')
    elif jogador == 2: #JOGADOR TESOURA
        print('JOGADOR VENCEU')
elif computador == 2: #CPU TESOURA
    if jogador == 0: #JOGADOR PEDRA
        print('JOGADOR VENCEU')
    elif jogador == 1: #JOGADOR PAPEL
        print('COMPUTADOR VENCEU')
    elif jogador == 2: #JOGADOR TESOURA
        print('EMPATE')