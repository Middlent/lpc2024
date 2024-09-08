import random


def rolagem(qtd_dados):
    contadores = [0, 0, 0, 0, 0, 0]
    for i in range(qtd_dados):
        contadores[random.randint(0, 5)] += 1
    return contadores


print(rolagem(100))
