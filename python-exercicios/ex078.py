valores = list()
menor = maior = 0
menor_p = list()
maior_p = list()

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

    if c == 0:
        menor = valores[c]
        menor_p.append(0)
        maior = valores[c]
        maior_p.append(0)
    else:
        if menor > valores[c]:
            menor = valores[c]
        if maior < valores[c]:
            maior = valores[c]

print(f'\nVoce digitou os valores {valores}')
print(f'\nO menor valor foi {menor} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=' ')
print()
print(f'O maior valor foi: {maior} e está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=' ')
