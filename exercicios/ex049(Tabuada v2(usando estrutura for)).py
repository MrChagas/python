print('Seja bem vindo a versão 2 da tabuada By MrChagas!\n')
n = int(input('Digite um número para ver a sua tabuada: '))
for t in range(1,11):
    print('{} x {:2} = {}'.format(n, t, n*t))
