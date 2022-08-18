print('Seja bem vindo a Calculadora de descontos by MrChagas')

price = float(input('\nQual é o preço do produto? R$'))
desc = float(input('\nQual é o valor do desconto aplicado? %'))
#desc = price - (price*0.05)
novo = price - (price * (desc/100))
print('\nO produto que custava R${:.2f}, na promoção com desconto de 5%, vai custar apenas R${:.2f}'.format(price, novo ))