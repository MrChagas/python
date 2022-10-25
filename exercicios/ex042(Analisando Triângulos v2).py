s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
print('\nOs dados inseridos foram {}, {} e {}'.format(s1,s2,s3))

if s1 < s2 + s3 and s2 < s1 +s3 and s3 < s1 + s2:
    print('\nOs segmentos acima PODEM FORMAR um triângulo:', end='')
    if  s1 == s2 == s3:
        print(' EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Não podem formar um triângulo')