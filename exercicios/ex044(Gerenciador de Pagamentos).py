print('='*12, 'CHAGASTORE', '='*12) #ou podemos usar: print('{:=^40'.format('CHAGASTORE')
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO'
[1] À VISTA DINHEIRO/PIX
[2] À VISTA NO CARTÃO
[3] ATÉ 3X NO CARTÃO
[4] 4X OU MAIS NO CARTÃO''')
opção = int(input('INFORME A SUA ESCOLHA:'))

if opção == 1:
    total = compras-(compras * 0.15)
    print('Sua compra terá um desconto de 15% pelo pagamento no dinheiro ou pix. Valor final: R${}'.format(total))
elif opção == 2:
    total = compras-(compras *0.10)
    print('Sua compra terá um desconto de 10% pelo pagamento à vista no cartão. Valor final: R${}'.format(total))
elif opção == 3:
    total = compras-(compras * 0.05)
    parcela2 = total /2
    parcela3 = total /3
    print('''Sua compra poderá ser parcelada em 
    1x de {:.2f} ou,
    2x de {:.2f} ou.
    3x de {:.2f} SEM JUROS'''.format(total,parcela2, parcela3))
elif opção == 4:
    print('''[1] parcelar em 4x
    [2] parcelar em 5x
    [3] parcelar em 6x
    [4] parcelar em 7x
    [5] parcelar em 8x
    [6] parcelar em 9x
    [7] parcelar em 10x''')

    oppar = int(input('Escolha sua opção de parcelamento: '))
    total = (compras * 0.15) + compras
    parcelas = total / oppar
    print('ESTE TIPO DE PARCELAMENTO ACARRETA JUROS. O VALOR FINAL FICA EM: {} parcelas de {:.2f}'.format(oppar, parcelas))

else:
    total = compras
    print('\033[0;31mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.\033[m')

print('\nSua compra de R${:.2f} vai ficar no valor de R${:.2f} no final do processo'.format(compras, total))