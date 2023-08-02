#Frases polindromo

sentence = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

if sentence == sentence[::-1]:
    print('A frase é um POLINDROMO')
else:
    print('A frase não é um POLINDROMO')

print('O inverso de {} é {}'.format(sentence, sentence[::-1]))
