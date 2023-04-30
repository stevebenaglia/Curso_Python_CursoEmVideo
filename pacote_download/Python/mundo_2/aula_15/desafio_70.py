'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''

total = totmil = menor = cont = 0
barato = " "

while True:
    produto = str(input("Nome do produto: \n"))
    preço = float(input("Preço: \n"))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 0 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Inserir mais produtos? [S / N] ")).strip().upper()[0]
    if resp == "N":
        print(f"Total gasto: R${total:.2f}")
        print(f"Produtos que custam mais do que R$1.000: {totmil}")
        print(f"O produto mais barato é {barato}, que custa R${menor:.2f}")
        break
