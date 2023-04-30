'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''
'''
counter = 1
tupla = []
# Ler 4 valores pelo teclado:
while counter < 5:
    n = int(input(f"Digite um número ({counter}/4): \n"))
    tupla.append(n)
    counter += 1
# guardá-los em uma tupla:
tupla = tuple(tupla)
print(f"Tupla: {tupla}")
# a) quantas vezes apareceu o valor 9
nove = tupla.count(9)
print(f"O valor 9 aparece {nove} vezes.")
# b) em que posição foi digitado o primeiro valor 3:
if 3 in tupla:
    print(f"O primeiro 3 está na posição: {tupla.index(3)+ 1}.")
else:
    print("O número 3 não está presente.")
# c) quais foram os números pares:
pares = []
for num in tupla:
    if num % 2 == 0:
        pares.append(num)
print(f"Números pares: {pares}")
'''
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores{núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.iindex(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitas foram ', end='')
for n in núm:
    if n % 2 ==0:
        print(n, end='')
        