'''
Crie um programa onde o usuário possa digitar
sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.

No final, mostre os valores pares e ímpares
em ordem crescente.
'''
lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}o. valor: "))
    if valor % 2 == 0:
        lista[0].append(valor)  # números pares
    else:
        lista[1].append(valor)  # números ímpares
print(f"Números pares em ordem crescente: {sorted(lista[0])}")
print(f"Números ímpares em ordem crescente: {sorted(lista[1])}")
