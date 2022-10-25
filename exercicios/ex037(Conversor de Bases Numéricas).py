num = int(input('Escolha um número inteiro para converter: '))
print('''Escolha uma das bases para conversão:
Para converter para BINÁRIO     [1]
Para converter para OCTAL       [2]
Para converter para HEXADECIMAL [3]''')
opc = int(input('Sua Opção: '))
if opc == 1:
    print('\n{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) #Esse [2:] usado é para fatiar a resposta e mostrar apenas o que aparece da terceira casa pra frente
elif opc == 2:
    print('\n{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('\n{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE')
