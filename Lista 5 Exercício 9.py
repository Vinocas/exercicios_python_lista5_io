'''
9.	Suponha que um caixa disponha apenas de notas de 1, 10 e 100 reais.
Considerando que alguém está pagando uma compra, escreva um algoritmo que mostre o número mínimo de notas que o caixa deve fornecer como troco. Mostre também: o valor da compra, o valor do troco e a quantidade de cada tipo de nota do troco. Suponha que o sistema monetário não utilize moedas.
'''

print('Digite o valor da compra: ')
compra = float(input())

print('Digite o valor pago: ')
pagamento = float(input())

while pagamento < compra:
    print('O valor pago deve ser maior que a compra. Digite novamente o valor pago: ')
    pagamento = int(input())

troco = float(pagamento - compra)

nota20 = int(troco / 20)
print('Quantidade de notas de R$20: ' + str(nota20))

troco = (troco % 20)

nota10 = int(troco / 10)
print('Quantidade de notas de R$10: ' + str(nota10))

troco = float(troco % 10)

nota1 = int(troco / 1)
print('Quantidade de notas de R$1: ' + str(nota1))

input()