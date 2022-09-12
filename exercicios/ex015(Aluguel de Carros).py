print('Seja Bem vindo a Calculadora de Alguel para carros by MrChagas')

d = int(input('\nPor quantos dias o carro foi alugado? '))
km = float(input('\nQuantos Km foram percorridos? '))

da = d * 60
kmr = km*0.15
total = da + kmr
print('\nO Aluguel deste carro sairá por R${:.2f}'.format(total))