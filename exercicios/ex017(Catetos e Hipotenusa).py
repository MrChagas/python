import math
print('Seja Bem vindo a Calculadora de Hipotenusa By MrChagas')
cao = float(input('Comprimento do Cateto Oposto: '))
caa = float(input('Comprimento do Cateto Adjacente: '))
#hip = (cao ** 2 + caa ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hip))

hip = math.hypot(cao, caa)
print('A hipotenusa vai medir {:.2f}'.format(hip))