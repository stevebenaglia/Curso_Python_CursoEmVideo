def dobro(num=0):
    return num * 2

def metade(num=0):
    return num / 2

def aumentar(num=0, taxa=0):
    resultado = num + (taxa * num / 100)
    return resultado

def diminuir(num=0, taxa=0):
    resultado = num - (taxa * num / 100)
    return resultado

def moeda(num = 0, moeda="R$"):
    return f"{moeda}{num:>.2f}".replace(".", ",")
