'''
3.	Maior entre três números: Ler três números diferentes e mostrar na tela uma mensagem indicando qual é o maior.
'''
print('Insira o primeiro número: ')
a = float(input())

print('Insira o segundo número: ')
b = float(input())

print('Insira o terceiro número: ')
c = float(input())

while a==b==c:
    print('Os números inseridos são iguais. Insira novamente os valores')
    print('Insira o primeiro número: ')
    a = float(input())

    print('Insira o segundo número: ')
    b = float(input())

    print('Insira o terceiro número: ')
    c = float(input())

if a > b and a > c:
    print('O maior número inserido é : ' + str(a) + '.')

elif b > a and b > c:
    print('O maior número inserido é : ' + str(b) + '.')

else:
    print('O maior número inserido é : ' + str(c) + '.')

input()