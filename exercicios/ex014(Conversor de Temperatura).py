print('Seja bem vindo ao conversor de Temperaturas by MrChagas')

GrausC = float(input('Informe a Temperatura em °C: '))

GrausF = (GrausC * 9/5) + 32
GrausK = GrausC + 273.15

print('\nA temperatura de {}ºC equivale a {}°F\n\nE esta temperatura em Kelvin vale {}ºK'.format(GrausC, GrausF, GrausK))