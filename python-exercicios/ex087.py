matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_3 = maior_2 = 0

for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
        
        if c == 2:
            soma_3 = soma_3 + matriz[l][c]

        if l == 1 and matriz[l][c] > maior_2:
            maior_2 = matriz[l][c]
        
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

print('-=-'*15)

for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=-'*15)

print(f'\nA soma dos valores pares é igual a: {soma_pares}')
print(f'A soma dos valores da 3ª coluna: {soma_3}')
print(f'O maior valor da segunda linha é: {maior_2}')

print('-=-'*15)