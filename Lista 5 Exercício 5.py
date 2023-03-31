'''
5.	Equação do segundo grau - Ler os coeficientes a, b e c de uma equação de segundo grau e, antes de calcular as raízes, calcular o valor de delta. Se este for negativo, informar que a equação não tem solução real. Se for zero, mostrar a única raiz. Se positivo, mostra as duas raízes.
'''
from cmath import sqrt


print('Insira o valor de a: ')
a = float(input())

print('Insira o valor de b: ')
b = float (input())

print('Insira o valor de c: ')
c= float(input())

delta = b**2-4*a*c

if delta < 0:
    print('O valor de Δ é ' + str(delta) + '. Logo, não tem solução real.')

elif delta == 0:
    print('O valor de Δ é ' + str(delta) + ' Logo, apresenta apenas uma raiz.')
    print('O valor de x é: ' + str(-b/2*a) + '.')

else:
    print('O valor de Δ é ' + str(delta) + '. Logo, apresenta duas raízes.')
    print('O valor de x1 é ' + str((-b+sqrt(delta))/2*a) + '.')
    print('O valor de x2 é ' + str((-b-sqrt(delta))/2*a) + '.')

input()