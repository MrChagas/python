n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media >= 7:
    print('O Aluno está aprovado!')
elif media >= 5 and media <7:
    print('O Aluno está de recuperação!')
elif media <5:
    print('O Aluno está reprovado!')