# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 5.29 = US$ 1
n = float(input("Quanto dinheiro você tem? \nR$"))
dolar = 5.29
conversao = n / dolar
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))
