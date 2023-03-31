'''
10.	Dado o valor do salário de um empregado, calcular e exibir o valor pago ao Imposto de Renda, considerando:

Salário em R$	Valor do Imposto
Salário <  100	Isento
100 ≤ Salário < 500	10%
500 ≤ Salário < 2000	18%
Salário ≥ 2000	25%
'''

print('Insira o valor do salário a ser calculado: ')
salario = float(input())

if salario < 100:
    print('O salário inserido é isento de imposto!')

elif salario >= 100 and salario < 500:
    print('O empregado deve 10% do salário. Sendo assim, o valor do imposto é: R$' + str(salario * 0.1))

elif salario >= 500 and salario < 2000:
    print('O empregado deve 18% do salário. Sendo assim, o valor do imposto é: R$' + str(salario * 0.18))

elif salario >= 2000:
    print('O empregado deve 25% do salário. Sendo assim, o valor do imposto é: R$' + str(salario * 0.25))

input()