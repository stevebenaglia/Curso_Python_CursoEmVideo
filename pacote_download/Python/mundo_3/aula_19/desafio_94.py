"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.
No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""
'''
person_dict = dict()
general_info, names, names_quantity, ages, women, above_mean = list(), list(), list(), list(), list(), list()
while True:
    # recebe nome:
    person_dict['name'] = input("Nome: \n")
    # recebe sexo:
    sex = input("Sexo [M/F]: \n")
    sex = sex[0].upper()
    person_dict['sex'] = sex
    # recebe idade:
    person_dict['age'] = float(input("Idade: \n"))
    # insere os dicionários na lista:
    general_info.append(person_dict.copy())
    # continuar ou sair?
    leave = input("Continuar? [S/N] \n")
    leave = leave.upper()
    if leave[0] == "N":
        break
for dictionary in general_info:
    # a.: quantas pessoas foram cadastradas:
    names_quantity.append(dictionary.get("name"))
    # b.: a média de idade do grupo:
    ages.append(dictionary.get("age"))
    age_mean = sum(ages)/len(ages)
    # c.: uma lista com todas as mulheres:
    for key, value in dictionary.items():
        if value == "F":
            women.append(dictionary.get("name"))
    # d.: uma lista com todas as pessoas com idade acima da média:
    if dictionary.get("age") > (age_mean):
        above_mean.append(dictionary.get("name"))
print(f"Pessoas cadastradas: {len(names_quantity)}")
print(f"Idade média do grupo: {age_mean:.1f} anos.")
print(f"Mulheres do grupo: {women}")
print(f"Pessoas com idade acima da média: {above_mean}")
'''
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper [0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N. ')
    if resp == 'S':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram: ', end ='')
for p in galera: 
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
   if p['idade'] >= média:
       for k, v in p.items():
           print(f'{k} = {v}; ', end='')
        