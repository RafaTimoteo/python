
soma = n = 0

while n != 999:
    n = int(input('Digite um número para somar: '))
    if n == 999:
        break
    else:
        soma = soma + n

# print('A soma é {}'.format(soma))
print(f'A soma é {soma}')