"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
'''
student_info = dict()
situação = ""
student_name = input("Nome do aluno: \n")
student_mean = float(input(f"Média de {student_name}: \n"))
student_info["name"] = student_name
student_info["mean"] = student_mean
print(f"O nome é igual a {student_name}.")
print(f"A média é igual a {student_mean}.")
if student_mean >= 6:
    situação = "aprovado"
elif student_mean >= 4 and student_mean <= 5.9:
    situação = "recuperação"
else:
    situação = "reprovado"
print(f"Situação é igual a {situação}.")
'''    
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] - float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média']< 7:
    aluno['situação'] = 'Recuperação'
else: 
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
