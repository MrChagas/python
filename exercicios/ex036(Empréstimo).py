casa = float(input('Valor da Casa: R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos dejesa financiar? '))
prestacao = casa / (anos * 12)
porcentagem = (sal * 0.30)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))

if prestacao <= porcentagem:
    print('\033[0;32mO empréstimo FOI APROVADO')
else:
    print('\033[0;31mO empréstimo NÃO FOI APROVADO')
