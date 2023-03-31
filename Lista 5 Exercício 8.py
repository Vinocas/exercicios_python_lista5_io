'''
8.	Triângulo no plano cartesiano: Dados as coordenadas x e y, digitados pelo usuário, de cada um dos 3 vértices de um triângulo qualquer, no plano cartesiano, calcular e exibir:
1.	Tamanho dos lados A, B e C
2.	Área do triângulo
3.	Perímetro do triângulo.
	Onde  d=sqrt((x2-x1)^2+(y2-y1)^2)
'''
from math import sqrt

print('Digite a coordenada x do lado A: ')
xA = float(input())

print('Digite a coordenada y do lado A: ')
yA = float(input())

print('Digite a coordenada x do lado B: ')
xB = float(input())

print('Digite a coordenada y do lado B: ')
yB = float(input())

print('Digite a coordenada x do lado C: ')
xC = float(input())

print('Digite a coordenada y do lado C: ')
yC = float(input())

AB = float(sqrt(xB-xA)**2+(yB-yA)**2)
BC = float(sqrt(xB-xC)**2+(yB-yC)**2)
AC = float(sqrt(xA-xC)**2+(yA-yC)**2)
sp = float(AB+BC+AC/2)

print('Distância AB = ' + str(AB))
print('Distância BC = ' + str(BC))
print('Distância AC = ' + str(AC))
print('A área do triângulo é igual a: ' + str(sqrt(sp*(sp-AB)*(sp-BC)*(sp-AC))))
print('O perímetro do triângulo é igual a: ' +str(AB+BC+AC))

input()