'''
4.	Divisão: Ler dois números e efetuar uma divisão, mas somente se o divisor for diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.
'''

print('Insira o dividendo da divisão: ')
dividendo = float(input())

print('Insira o divisor da divisão: ')
divisor = float(input())

while divisor == 0:
    print('O divisor deve ser diferente de 0.')
    print('Insira outro valor para o divisor da divisão: ')
    divisor = float(input())

resultado = dividendo/divisor

print('O resultado da divisão é: ' + str(resultado) + '.')

input()