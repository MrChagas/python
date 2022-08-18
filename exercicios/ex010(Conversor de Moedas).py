print('Seja Bem vindo ao Conversor de moedas by MrChagas')

dol = float(input('\nQuanto está valendo o dolar atualmente?\n'))
real = float(input('\nQuanto dinheiro você tem disponível?\n'))

conv = real / dol

print('\nVocê sabia que com seus R${:.2f} e com a cotação do dolar em US${} você teria exatos US${:.2f}?'.format(real, dol, conv))