print('Calculadora de Dobro, Triplo e Raíz Quadrada by MrChagas')

n = int(input('Digite um número qualquer: '))

do = n * 2
tr = n * 3
rq = n ** (1/2)

print('Sua escolha foi o número {}'.format(n))
print('Você sabia que o dobro dele equivale a {}'.format(do))
print('Seu triplo é igual a {}'.format(tr))
print('Sua raiz quadrada é igual a {:.4f}'.format(rq))