import math
print('\nSeja Bem vindo a calculadora de Seno, Cosseno e Tangente By MrChagas')
an = float(input('\nDigite o ângulo que você tem: '))
sen = math.sin(math.radians(an))
print('\nO ângulo de {:.0f} tem o SENO de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('\nO ângulo de {:.0f} tem o COSSENO de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('\nO ângulo de {:.0f} tem a TANGENTE de {:.2f}'.format(an, tan))