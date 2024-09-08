def num_to_extenso(num):
    text_num = str(num)
    resposta = ""
    if len(text_num) > 2 or text_num[0] not in "0123456789" or (len(text_num) > 1 and text_num[1] not in "0123456789"):
        return "Apenas números até 99 suportados"
    elif len(text_num) > 1:
        if text_num[0] == "1":
            if text_num[1] == "0":
                return "Dez"
            elif text_num[1] == "1":
                return "Onze"
            elif text_num[1] == "2":
                return "Doze"
            elif text_num[1] == "3":
                return "Treze"
            elif text_num[1] == "4":
                return "Quatorze"
            elif text_num[1] == "5":
                return "Quinze"
            elif text_num[1] == "6":
                return "Dezesseis"
            elif text_num[1] == "7":
                return "Dezessete"
            elif text_num[1] == "8":
                return "Dezoito"
            elif text_num[1] == "9":
                return "Dezenove"
        elif text_num[0] == "2":
            resposta = "Vinte"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "3":
            resposta = "Trinta"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "4":
            resposta = "Quarenta"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "5":
            resposta = "Cinquenta"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "6":
            resposta = "Sessenta"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "7":
            resposta = "Setenta"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "8":
            resposta = "Oitenta"
            if (text_num[1] != "0"):
                resposta += " e "
        elif text_num[0] == "9":
            resposta = "Noventa"
            if (text_num[1] != "0"):
                resposta += " e "
        if text_num[1] == "1":
            resposta += "um"
        elif text_num[1] == "2":
            resposta += "dois"
        elif text_num[1] == "3":
            resposta += "tres"
        elif text_num[1] == "4":
            resposta += "quatro"
        elif text_num[1] == "5":
            resposta += "cinco"
        elif text_num[1] == "6":
            resposta += "seis"
        elif text_num[1] == "7":
            resposta += "sete"
        elif text_num[1] == "8":
            resposta += "oito"
        elif text_num[1] == "9":
            resposta += "nove"
    else:
        if text_num[0] == "0":
            resposta += "Zero"
        elif text_num[0] == "1":
            resposta += "Um"
        elif text_num[0] == "2":
            resposta += "Dois"
        elif text_num[0] == "3":
            resposta += "Tres"
        elif text_num[0] == "4":
            resposta += "Quatro"
        elif text_num[0] == "5":
            resposta += "Cinco"
        elif text_num[0] == "6":
            resposta += "Seis"
        elif text_num[0] == "7":
            resposta += "Sete"
        elif text_num[0] == "8":
            resposta += "Oito"
        elif text_num[0] == "9":
            resposta += "Nove"
    return resposta

print(num_to_extenso(input("Insira um número de 0 a 99: ")))
