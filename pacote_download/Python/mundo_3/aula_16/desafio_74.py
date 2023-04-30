'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''
from random import randint
'''
# gerar 5 números e colocar numa tupla:
tupla = []
counter = 0
while counter < 5:
    tupla.append(randint(0, 100))
    counter += 1
tupla = tuple(tupla)
# listagem de números gerados:
print("Valores sorteados: ", end="")
for num in tupla:
    print(f"{num} ", end="")
# menor e maior valores:
menor = tupla[0]
maior = tupla[0]
for num in tupla:
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print(f"\nMenor: {menor}")
print(f"Maior: {maior}")
'''
numeros = (randint(1,10), randint(1,10), randint(1,10), 
           randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end= '')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'\nO menor valor sorteado foi {min(numeros)}')
