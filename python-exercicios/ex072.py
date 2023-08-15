# Número por extenso

choice = 'S'
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        user = int(input('Digite um número entre 0 e 20: '))
        if 0 <= user <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'O número digitado foi {num[user]}')
    while True:
        choice = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if choice in 'SsNn':
            break
        print('Tente novamente. ', end='')
    if choice in 'Nn':
        break

print('Fim do programa. Volte sempre!')