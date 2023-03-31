'''
7.	Ano bissexto - Um ano é bissexto se for divisível por 4 exceto os séculos, que são bissextos se forem múltiplos de 400. Escreva um programa que determina se um ano é bissexto.
'''

print('Insira o ano: ')
ano = int(input())

if ano % 4 == 0:

    if ano % 100 == 0:

        if ano % 400 == 0:
            print(str(ano) + ' é um ano bissexto!')

        else:
            print(str(ano) + ' não é um ano bissexto!')
    
    else:
        print(str(ano) + ' é um ano bissexto!')

else:
    print(str(ano) + ' não é um ano bissexto!')

input()