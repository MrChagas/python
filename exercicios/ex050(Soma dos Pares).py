soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num %2 ==0:
        soma = soma + num   # A soma de todos os números que aparecem em num
        cont = cont + 1     # Conta quantos números terão na soma
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))