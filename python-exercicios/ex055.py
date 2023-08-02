#maior peso
kgmaior = 0
pmaior = 0
kgmenor = 0
pmenor = 0
for pess in range(1, 6):
    peso = float(input('Qual o peso da {}º pessoa em kg'.format(pess)))
    if peso > kgmaior:
        kgmaior = peso
        pmaior = pess
    elif peso < kgmenor:
        kgmenor = peso
        pmenor = pess
    
print(kgmaior)
print(pmaior)
print('-'*5)
print(kgmenor)
print(pmenor)
