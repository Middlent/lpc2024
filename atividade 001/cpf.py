def get_validator(cpf_numbers):
    soma = 0
    multi = len(cpf_numbers) + 1
    for i in range(len(cpf_numbers)):
        soma += int(cpf_numbers[i]) * multi
        multi -= 1
    if soma // 11 > 2:
        return str(11 - (soma % 11))
    else:
        return "0"


def valida_cpf(cpf):
    try:
        cpf_code, validador = cpf.split('-')
        cpf_sep = cpf_code.split('.')
        if(len(cpf_sep) == 3):
            cpf_numbers = cpf_sep[0] + cpf_sep[1] + cpf_sep[2]
            validador_true = get_validator(cpf_numbers)
            validador_true += get_validator(cpf_numbers+validador_true)
            if validador_true == validador:
                return "CPF válido"
        return "CPF inválido"
    except:
        return "CPF inválido"

print(valida_cpf(input("Insira seu CPF (Em formato xxx.xxx.xxx-xx): ")))
