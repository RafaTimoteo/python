# contando vogais

palavras = ('mercado', 'python', 'sanduiche', 'magica')

for item in palavras:
    print(f'\nNa palavra {item.upper()} temos:', end='')
    for l in item:
        if l.lower() in 'aeiou':
            print(l, end=' ')
