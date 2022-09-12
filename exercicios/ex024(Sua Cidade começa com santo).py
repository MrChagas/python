print('Olá! Vamos verificar as primeiras letras de um texto by MrChagas\n')

cid = str(input('Em qual cidade você nasceu? ')).strip() #Cidade
nc = cid.capitalize() #nomeCerto
print('Santo' in nc)