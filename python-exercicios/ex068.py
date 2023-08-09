from random import randint

v = 0

while True:
    user = int(input('Digite um número: '))
    pc = randint(0, 10)
    total = user + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {user} e o computador {pc}, total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            v = v + 1
        else:
            print('VOCE PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
        else:
            print('VOCE PERDEU!')
            break

    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v}')
