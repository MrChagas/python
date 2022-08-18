print('Bem vindo a Calculadora de latas de tinta by MrChagas')

lar = float(input('Digite a Largura da parede: '))
alt = float(input('Digite a Altura da Parede: '))
area = lar*alt
tinta = area/2
print('Sua parede tem dimensão de {}m x {}m e sua area total é de {:.2f}m²'.format(lar, alt, area))
print('Levando em consideração que cada litro de tinta pinta 2m². Para pintar essa parede você precisará de {:.2}l de tinta. '.format(tinta))