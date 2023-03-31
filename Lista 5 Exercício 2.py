'''
2.	Maior entre dois números: Ler dois números inteiros, quaisquer e mostrar na tela uma
mensagem indicando qual é o maior, ou se são iguais.
'''
print('Digite o primeiro número: ')
a = int(input())
print('Digite o segundo número: ')
b = int(input())

while a==b:
    print('Os dois números são iguais, digite novamente os valores.')
    print('Digite o primeiro número: ')
    a = int(input())
    print('Digite o segundo número: ')
    b = int(input())

if a>b:
    print('O maior número é: ' + str(a) + ".")

else:
    print('O maior número é: ' + str(b) + ".")

input()
