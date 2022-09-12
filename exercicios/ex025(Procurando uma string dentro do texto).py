print('Olá! Vamos pesquisar uma palabra específica numa frase by MrChagas!')
nome = str(input('Qual é o seu nome completo? ')).strip()
nc = nome.title()
n = 'Silva' in nc

print('Seu nome tem Silva? {}' .format(n))