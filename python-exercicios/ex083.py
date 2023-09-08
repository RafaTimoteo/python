expr = str(input('Digite sua expressão: '))
pilha = list()

for c in expr:
    if c == '(':
        pilha.append('(')

    elif c == '(':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')

