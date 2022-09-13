from time import sleep
print('Seja bem vindo a calculadora de Reajuste Salarial by MrChagas')

sal = float(input('Informe seu salário atual: '))

print('\nLigando para o Patrão...')
sleep(2)
print('Puxando saco e pedindo o aumento...\n')
sleep(4)

if sal < 1250:
    q = (sal * 0.15) + sal
    print('Depois de puxar o saco, o seu novo salário será R${:.2f}'.format(q))
if sal > 1251 and sal < 1999:
    d = (sal * 0.10) + sal
    print('Depois de puxar o saco, o seu novo salário será R${:.2f}'.format(d))
if sal > 2000:
    c = (sal * 0.05) + sal
    print('Depois de puxar o saco, o seu novo salário será R${:.2f}'.format(c))