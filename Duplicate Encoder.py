"""Цель этого упражнения состоит в том, чтобы преобразовать строку в новую строку, где каждый символ в новой строке является "("тем, если этот символ появляется только один раз в исходной строке или ")"если этот символ появляется более одного раза в исходной строке.
Игнорируйте заглавные буквы при определении того, является ли символ дубликатом."""

def dublicate_encode(word):
    new_word=''
    for i in word.lower():
        if word.lower().count(i)==1:
            new_word+='('
        else:
            new_word+=')'
    return new_word
print(dublicate_encode('hello'))


