from time import sleep

print('Bem vindo a Calculadora de Passagens by MrChagas')

d = int(input('Qual vai ser a distancia da sua viagem?(Em Km) '))
print('\nPechinchando valores...')
sleep(2)
print('Encontrando a companhia mais barata para você...\n')
sleep(2)
p1 = d * 0.50
p2 = d * 0.45
if d <= 200:
    print('Sua viagem vai sair pelo preço de R${:.2f}'.format(p1))
else:
    print('Sua viagem vai sair pelo preço de R${:.2f}'.format(p2))