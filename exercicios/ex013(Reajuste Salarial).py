print('Seja bem vindo a calculadora de reajuste salarial by MrChagas')

sal = float(input('Qual o salarário atual do Funcionário? R$'))
reaj = float(input('Qual será a porcentagem de reajuste? '))
saln = (sal*(reaj / 100)) + sal

print('Um funcionário que ganhava R${}, com 15% de aumento, passará a receber R${:.2f}'.format(sal, saln))