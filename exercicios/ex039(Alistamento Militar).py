#Importar a biblioteca datetime, ou a função date, para calcular o ano atual automaticamente.
from datetime import date

#Opção para encontar o ano atual
atual = date.today().year

#Variável ano de nascimento
nasc = int(input('Digite seu Ano de Nascimento: '))

#Variável Ano

#Variável idade
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

#Condições
if idade > 18:
    print('\nVocê deveria ter se alistado há {} anos.'.format(idade-18))
    print('Já passou da hora de se alistar!')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
    print('Seu alistamento será no ano de {}'.format(atual+(18-idade)))
else:
    print('Nada')