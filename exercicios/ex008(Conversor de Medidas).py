print('****** Sejam bem vindos ao conversor de medidas By MrChagas ******')
m = float(input('Digite uma distancia em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('\nA medida inserida foi de {}m e corresponde a:'.format(m))
print('{}Km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))