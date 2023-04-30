# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada

n = int(input("Digite um número: \n"))
print("Tabuada do {}:".format(n))

print("{} x {} = {}".format(n, 1, (n * 1)))
print("{} x {} = {}".format(n, 2, (n * 2)))

# Sem loop o código é repetitivo
