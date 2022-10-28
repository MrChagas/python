soma = 0 #Acumulador
cont = 0 #Conta quantos números serão escritos em num
for num in range(1, 501, 2):
    if num % 3 == 0: #Se o número for divisível por 3
    #print(c, end=' ') #Contagem dos Múltiplos de 3
        soma = soma + num #A soma de todos os números que aparecem em num
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))