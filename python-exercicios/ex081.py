valores = list()
choice = 'S'
tot5 = 0

while True:
    if choice in 'Ss':
        valores.append(int(input('Digite um valor: ')))
        if valores[-1] == 5:
            tot5 += 1
        choice = str(input('Quer adicionar mais? [S/N] ')).strip().upper()[0]
        if choice not in 'SsNn':
            choice = str(input('Quer adicionar mais? [S/N] ')).strip().upper()[0]
    elif choice in 'Nn':
        break

print(f'\nVoce digitou {len(valores)} elementos')
print(f'os valores em ordem decrescente sào: {sorted(valores, reverse=True)}')
if tot5 > 0:
    print(f'Quantidade de vezes que o numero 5 aparece: {tot5}')
else:
    print('Voce nao digitou o numero 5')
