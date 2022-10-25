from datetime import date

ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano

print('O atleta tem {} anos'.format(idade))

if idade > 0 and idade < 9:
    print('Classificação: Mirim')
elif idade > 10 and idade < 14:
    print('Classificação: Junior')
elif idade > 15 and idade < 19:
    print('Classificação: Juvenil')
elif idade > 19 and idade < 25:
    print('Classificação: Sênior')
elif idade > 25:
    print('Classificação: Master')