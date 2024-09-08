import random


def mostrar_palavra_ocultada(palavra, letras_encontradas):
    palavra_ocultada = ""
    for letra in palavra:
        if letra not in letras_encontradas:
            palavra_ocultada += " _"
        else:
            palavra_ocultada += " "+letra.upper()

    print("A palavra é:"+palavra_ocultada)

file = open("br-sem-acentos.txt", "r", encoding="UTF-8")
palavra = random.choice(file.readlines()).strip()
file.close()

qtd_letras = set()
for letra in palavra:
    qtd_letras.add(letra)

letras_encontradas = ""
letras_tentadas = ""
erros = 0
encontrou = False

while(len(letras_encontradas) + len(letras_tentadas) < len("qwertyuiopasdfghjklçzxcvbnm") and not encontrou):
    mostrar_palavra_ocultada(palavra, letras_encontradas)
    print("Letras tentadas: "+letras_tentadas)
    letra_tentada = input("Digita uma letra: ").lower()
    if len(letra_tentada) > 1 or letra_tentada not in "qwertyuiopasdfghjklçzxcvbnm":
        print("Letra inválida")
    elif letra_tentada in letras_tentadas or letra_tentada in letras_encontradas:
        print("Letra já tentada")
    else:
        if letra_tentada in palavra:
            letras_encontradas += letra_tentada
            if len(letras_encontradas) == len(qtd_letras):
                encontrou = True
        else:
            letras_tentadas += letra_tentada.upper()
            erros += 1
            print("Errado, esse é seu erro número", erros)

print("A palavra final era "+palavra)
