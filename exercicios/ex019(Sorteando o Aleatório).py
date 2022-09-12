import random

#c = Candidato

c1 = input('Nome do Primeiro Candidato: ')
c2 = input('Nome do Segundo Candidato: ')
c3 = input('Nome do Terceiro Candidato: ')
c4 = input('Nome do Quarto candidato: ')
lista = [c1, c2, c3, c4]
sorteado = random.choice(lista)
print('O candidato escolhido foi {}'.format(sorteado))