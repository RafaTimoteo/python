pessoa = list()
conj = list()
morefat = list()
maior = 0
menor = float('inf')

while True:
     pessoa.append(str(input('Nome: ')))
     pessoa.append(float(input('Peso(kg): ')))
     conj.append(pessoa[:])
     
     if pessoa[1] > maior:
          maior = pessoa[1]
     
     if pessoa[1] < menor:
          menor = pessoa[1]
     
     pessoa.clear()
     
     choice = str(input('Deseja continuar? [S/N]  ')).strip().upper()[0]
     if choice in 'Nn':
          break

print('-=-'*25)

print(f'Ao todo, foram cadastrados {len(conj)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de: ', end='')
for p in conj:
     if p[1] == maior:
          print(f'[{p[0]}]')

print(f'O menor peso foi de {menor}kg. Peso de: ', end='')
for p in conj:
     if p[1] == menor:
          print(f'[{p[0]}]')  