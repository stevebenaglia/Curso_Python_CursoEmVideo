'''
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:

a: quantas pessoas foram cadastradas.
b: uma listagem com as pessoas mais pesadas
c: uma listagem com as pessoas mais leves

Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.

'''
'''
lista = list()
listb = list()
counter = 0
while True:
    lista.append(str(input("Nome: \n"))) 
    lista.append(float(input("Peso (em kg): \n")))
    listb.append(lista[:])
    lista.clear()
    counter += 1
    pergunta = str(input("Continuar? [Sim/Não] \n")).upper()
    if pergunta[0] == "N":
        break
print(f"a) pessoas cadastradas: {counter}.")
pesos = list()  
for i in listb:
    pesos.append(i[1])
pesos = sorted(pesos)  
menor = pesos[0]
maior = pesos[-1]
mais_pesados = list()
menos_pesados = list()
for k in listb: 
    if k[1] == maior:  
        mais_pesados.append(k[0])  
    if k[1] == menor:  
        menos_pesados.append(k[0])  
print(f" b) O maior peso foi de {maior}kg. Peso de {mais_pesados}")
print(f" c) O menor peso foi de {menor}kg. Peso de {menos_pesados}.")
'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg, Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end = '')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
