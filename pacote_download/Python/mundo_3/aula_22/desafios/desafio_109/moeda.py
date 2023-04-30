def dobro(num=0, is_formatted=False):
    resultado = num * 2
    return resultado if is_formatted is False else moeda(resultado)

def metade(num=0, is_formatted=False):
    resultado = num / 2
    return resultado if is_formatted is False else moeda(resultado)

def aumentar(num=0, taxa=0, is_formatted=False):
    resultado = num + (taxa * num / 100)
    return resultado if is_formatted is False else moeda(resultado)

def diminuir(num=0, taxa=0, is_formatted=False):
    resultado = num - (taxa * num / 100)
    return resultado if is_formatted is False else moeda(resultado)

def moeda(num, moeda="R$"):
    return f"{moeda} {num:.2f}".replace(".", ",")
