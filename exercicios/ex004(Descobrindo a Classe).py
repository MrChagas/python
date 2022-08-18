print('Classe do elemento By MrChagas')

print('_'*22)
print('Qual a classe do que está escrito?')
a = input('Digite uma Palavra: ')

print('O tipo primitivo deste valor é: ',type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Está em Maiúsculas? ', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada? (Maiúsculas e minusculas juntas) ' ,a.istitle())

print('_'*22)