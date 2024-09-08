
def checa_palindromo(word):
    formated_word = ""
    formated_reverse_word = ""
    for letter in word:
        if letter.lower() in "qwertyuiopasdfghjklçzxcvbnm":
            formated_word += letter.lower()
            formated_reverse_word = letter.lower() + formated_reverse_word
    return formated_reverse_word == formated_word


word = input()
print(checa_palindromo(word))
