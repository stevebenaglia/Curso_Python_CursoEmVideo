'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
'''
lista = []
while True:
    num = int(input("Digite um número: \n"))
    if num in lista:
        print("O número já está na lista.")
    else:
        lista.append(num)
        print("Adicionado com sucesso...")
    keep = str(input("Quer continuar [SIM / NÃO]? \n")).strip().upper()
    if keep[0] == "N":
        break
    elif keep[0] == "S":
        print("Continuando.")
    else:
        print("Digite apenas 'sim' ou 'não'!")
lista.sort()
print(f"Você digitou os valores {lista}!")
'''
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicinar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
números.sort()
print(f'Você digitous os valores {números}')