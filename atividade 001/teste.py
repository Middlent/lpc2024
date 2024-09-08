import random

file = open("br-sem-acentos.txt", "r", encoding="UTF-8")
palavra = random.choice(file.readlines()).strip()
file.close()

numero = input()

dezena = numero[0]
unidade = numero[1]

resposta = ""

if(dezena == "2"):
    resposta += "Vinte"
    if unidade != 0:
        resposta += " e "
elif(dezena == "3"):
    resposta += "Trinta"

if(dezena != "1"):
    if(unidade == "1"):
        resposta += "um"















string = ""
letrasacertadas = ""

for letra in palavra:
    if letra in letrasacertadas:
        string += " "+letra
    else:
        string += " _"

letra = input()
if letra in palavra:
    letrasacertadas += letrasacertadas