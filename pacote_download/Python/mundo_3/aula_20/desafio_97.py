"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.
"""
def escreva(texto):
    tamanho = len(texto) + 4
    print("~" * tamanho)    
    print(f"  {texto}")
    print("~" * tamanho)    
escreva("Gustavo Guanabara")
escreva("Curso de Python no YouTube")
escreva("CeV")