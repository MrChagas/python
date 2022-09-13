n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha mais um número: '))
n3 = int(input('Escolha um último número: '))
#Maior
if n1 > n2 and n1 > n3:
    print('O MAIOR número é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O MAIOR número é {}.'.format(n2))
if n3 > n1 and n3 > n2:
    print('O MAIOR número é {}'.format(n3))
#Menor
if n1 < n2 and n1 < n3:
    print('O MENOR número é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O MENOR número é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O MENOR número é {}'.format(n3))