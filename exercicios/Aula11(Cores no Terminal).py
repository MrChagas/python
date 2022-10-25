# Para representar uma cor no python, Usar: \033[style:texto:fundo m
                                            #\033[0:33:44m
#Códigos para Style: #0 sem nada
                     #1 Bold (negrito)
                     #4 underline (sublinhado)
                     #7 negativo

#Códigos para Text: #30 Branco
                    #31 Vermelho
                    #32 Verde
                    #33 Amarelo
                    #34 Azul
                    #35 Roxo
                    #36 Cyano
                    #37 Cinza (Padrão)

#Códigos para Back  #40 Branco
                    #41 Vermelho
                    #42 Verde
                    #43 Amarelo
                    #44 Azul
                    #45 Roxo
                    #46 Cyano
                    #47 Cinza (Padrão)

print('\033[0;30;41mTeste De Cores\033[m')
print('\033[4;33;44mTeste De Cores\033[m')
print('\033[1;35;43mTeste De Cores\033[m')
print('\033[30;42mTeste De Cores\033[m')
print('\033[mTeste De Cores\033[m')
print('\033[7;30mTeste De Cores\033[m')