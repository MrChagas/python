print('Seja bem vindo ao Analisador de Triangulos by MrChagas')

print('=-='*20)
print('Analisador De Triangulos')
print('-=-'*20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Valores Acima podem formar um triangulo!')
else:
    print('Os Valores Acima não podem formar um triângulo!')