lista = list()

for c in range(0,5):
  v = int(input('Digite um valor: '))
  if c == 0 or v > lista[len(lista)-1]:
    lista.append(v)
    print(f'Valor adicionado no final da lista...')
  else:
    pos = 0
    while pos < len(lista):
      if v < lista[pos]:
        lista.insert(pos, v)
        print(f'Valor adicionado na posição {pos}...')
        break
      pos += 1

print(f'\nA lista completa é: {lista}') 