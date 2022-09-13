from time import sleep

print('Cuidado, você está passando por um Radar de Velocidade!')

v = int(input('Qual a Velocidade atual do seu carro? '))
print('\nCalculando a Velocidade...')
sleep(2)
multa = (v - 80) * 7
if v <= 80:
    print('\nCerto! Você está dentro do limite de velocidade. Tenha um bom dia!')
else:
    print('\nHAHA! Te flagrei a {}km/h. E você foi multado em R${:.2f} '.format(v, multa))