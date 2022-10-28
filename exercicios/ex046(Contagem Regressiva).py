from time import sleep
print('CHEGAMOS NO REVEILLON')
ano = int(input('Qual o ano atual?'))
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('FELIZ {}!! FELIZ ANO NOVO!'.format(ano+1))