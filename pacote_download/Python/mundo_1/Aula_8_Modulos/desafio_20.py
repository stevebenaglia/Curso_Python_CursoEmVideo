# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
shuffle(nomes)
print("A lista de apresentação é {}.".format(nomes))
