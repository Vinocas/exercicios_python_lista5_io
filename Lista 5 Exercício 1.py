'''
1.	Construa um aplicativo que verifique e mostre ao usuário  qual combustível compensa
utilizar em um automóvel “flex”. Sabe-se que a relação entre o preço do  álcool e o preço da
gasolina é 0,7.
'''
precoAlc = float(input('Insira o preço do álcool: '))
precoGas = float(input('Insira o preço da gasolina: '))

if (precoAlc/precoGas) <= 0.7:
    print('A razão entre os valores é menor ou igual a 0.7. Abasteça com álcool!') 
    
else:
    print('A razão entre os valores é maior que 0.7. Abasteça com gasolina!')

input()
