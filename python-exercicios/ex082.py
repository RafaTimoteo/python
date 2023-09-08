totlista = list()
listapar = list()
listaimpar = list()
choice = 'S'

while True:
    if choice in 'Ss':
        totlista.append(int(input('Digite um numero: ')))
        choice = str(input('Deseja adicionar mais? [S/N] ')).strip().upper()[0]
    elif choice in 'Nn':
        break
    else:
        choice = str(input('Deseja adicionar mais? [S/N] ')).strip().upper()[0]

for v in totlista:
    if (v % 2) == 0:
        listapar.append(v)
    elif (v % 2) == 1:
        listaimpar.append(v)
    else:
        print('Osh, entendi foi nada KKKKKKK')

print(f'\nLista completa: {totlista}')
print(f'Só os números pares: {listapar}')
print(f'Só os números ímpares: {listaimpar}')
