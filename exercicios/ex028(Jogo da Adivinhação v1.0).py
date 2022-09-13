import random
import time

print('Bem Vindo ao jogo da adivinhação by MrChagas')
print('-=-'*22)
comp = random.randint(0,5)
print('Estou pensando em um numero entre 0 e 5. Quer tentar a sorte?')
print('-=-'*22)
print('Faça a sua aposta! ')
aposta = int(input('\nSeu número: '))
print('PROCESSANDO...')
time.sleep(3)
if aposta == comp:
    print('\nPARABÉNS! Você venceu essa!')
else:
    print('VOCÊ PERDEU! Eu pensei no número {} e não no {}'.format(comp, aposta))
