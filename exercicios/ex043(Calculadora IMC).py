peso = float(input('Qual é o seu peso: (Kg) '))
altura = float(input('Qual a Sua altura? (m) '))
imc = peso /(altura**2)

print('Seu índice de IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('Você está com o PESO IDEAL')
elif imc > 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc > 30 and imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')