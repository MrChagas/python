#Funcionalidades de Análise de texto

frase = str('Curso em Video Python')
print('Ex 1', frase[9]) #Mostra o caractere 9 da frase
print('Ex 2', frase[9:13]) #mostra tudo o que tem entre o campo 9 e 13, porém o caractere 13 não aparece
print('Ex 3', frase[9:21]) #mostra tudo o que tem entre o campo 9 e 21, para não cortar a ultima letra/caractere
print('Ex 4', frase[9:21:2]) #mostra tudo o que tem entre o campo 9 e 21 pulando 2 casas
print('Ex 5', frase[:5]) #mostra tudo o que vem antes do campo 5 e para nele
print('Ex 6', frase[15:]) #Mostra apenas o que começa a partir do campo 15
print('Ex 7', frase[9::3]) #Mostra apenas o que está dentro do intervalo pulando 3 casas
print('Ex 8', len(frase)) #mostra o tamanho da frase com todos os caracteres
print('Ex 9', frase.count('o')) #conta quantas vezes aparece a letra 'o' dentro da frase
print('Ex10', frase.find('Android')) #Procura a palavra na frase, caso não tenha ele aparece -1
print('Ex11', 'Curso' in frase) #Mostra True ou false, caso tenha ou não a palavra nessa frase


#Funcionalidades de Transformação de texto

frase2 = str('  Curso em video Python   ')
print('Ex12', frase2.replace('Python','Android')) #Trocar a palavra Python por Android quando executar o código
print('Ex13', frase2.upper()) #tudo maiúsculo
print('Ex14', frase2.lower()) #tudo minúsculo
print('Ex15', frase2.capitalize()) #apenas a primeira letra da frase em maiúsculo
print('Ex16', frase2.title()) #deixar as primeiras letras de cada palavra em maiúsculo
print('Ex17', frase2.strip()) #Corta os espaços adicionais antes e no fim da frase
print('Ex18', frase2.rstrip()) #Corta os espaços adicionais que estão apenas do lado direito
print('Ex19', frase2.lstrip()) #Corta os espaços adicionais que estão apenas do lado esquerdo


#Funcionalidade de Divisão de texto
frase3 = str('Curso em Video 2022')
print('Ex20', frase3.split())

#Ao usar Aspas duplas 3 vezes, você seleciona um texto inteiro rapidamente