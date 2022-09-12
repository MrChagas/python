print('Olá, seja bem vindo ao Analisador de Nomes by MrChagas')

nomec = str(input('\nDigite seu nome completo: ')).strip()
print('\nUm momento. Analisando o seu nome...')

print('\nSeu nome todo em maiúsculo ficaria é: {}'.format(nomec.upper()))
print('\nJá seu nome todo em minúsculo é: {}'.format(nomec.lower()))
print('\nSeu nome completo tem {} letras' .format(len(nomec) - nomec.count(' '))) #esse espaço dentro da aspas de .count é até onde o programa vai contar caracteres antes de chegar no primeiro espaço
#print('Seu Primeiro nome tem {} letras'.format(nomec.find(' '))) #Nesse find, ele vai contar até chegar no primeiro espaço e vai trazer o tamanho do que está escrito antes do espaço

separa = nomec.split()
print('\nSeu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))