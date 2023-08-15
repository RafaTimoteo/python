lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis

for comida in lanche:
    print(f'Eu vou comer {comida}')

for count in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[count]} na posição {count}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi demais, c é loko')