import random

print('Seja bem vindo ao Sorteador de Ordem de Apresentação by MrChagas')

print('\nDigite abaixo os grupos disponíveis.')
g1 = input('Primeiro Grupo: ')
g2 = input('Segundo Grupo: ')
g3 = input('Terceiro Grupo: ')
g4 = input('Quarto Grupo: ')

lista = [g1, g2, g3, g4]
random.shuffle(lista)
print('A ordem de apresentação será a seguinte:')
print(lista)