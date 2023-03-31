'''
6.	Triângulo: Dados 3 valores  inteiros A, B e C, digitados pelo usuário, verificar se representam um triângulo. Lembre-se que, se A, B e C são lados de um triângulo se e somente se, as medidas dos lados atendem à seguinte expressão: (A<B+C) e (C<A+B) e (B<A+C).
Em caso positivo, 
•	exibir sua classificação quanto aos lados (eqüilátero, isósceles ou escaleno) e seu perímetro.
•	Calcular e exibir seu perímetro.
•	Calcular e exibir sua área.
Lembre-se que para calcular a área do triângulo, use a fórmula de Herão:   Area=sqrt(sp*(sp-A)*(sp-B)*(sp-C))  onde sp=(A+B+C)/2
'''

from math import sqrt

print('Insira o valor do lado A: ')
a = int(input())

print('Insira o valor do lado B: ')
b = int(input())

print('Insira o valor do lado C: ')
c = int(input())

perimetro = a+b+c
sp = float(a+b+c)/2
area = sqrt(sp* (sp-a) * (sp-b) * (sp-c))

if a<b+c and c<a+b and b<a+c:
    print('Os valores inseridos correspondem aos 3 lados de um triângulo!')

    if a==b and b==c and a==c:
        print('E se trata de um triânguo equilátero.')

    elif a!=b and b!=c and a!=c:
        print('E se trata de um triângulo escaleno.')

    else:
        print('E se trata de um triângulo isósceles.')
    
    print('O perimetro do triângulo é: ' + str(perimetro) + '.')
    print('A área do triângulo é: ' + str(area) + '.')

else:
    print('Os valores inseridos não correspondem aos 3 lados de um triângulo!')

input()
