# Cadastro de pessoas

maior_18 = men = women_sub20 = count = 0

while True:
    print('-=-'*15)
    print('CADASTRE UMA PESSOA')
    print('-=-'*15)
    i = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sex != 'M' and sex != 'F':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    count = count + 1
    if i >= 18:
        maior_18 = maior_18 + 1
    if sex == 'M':
        men = men + 1
    if i < 20 and sex == 'F':
        women_sub20 = women_sub20 + 1
    choice = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    while choice != 'S' and choice != 'N':
        choice = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if choice in 'Nn':
        break

print('-=-'*15)
print(f'Foram cadastrados {count} pessoas')
print(f'{maior_18} maior de idade')
print(f'{men} do sexo masculino')
print(f'{women_sub20} do sexo masculino abaixo dos 20 anos')
print('-=-'*15)
