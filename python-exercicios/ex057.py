
sex = str(input('Informe seu sexo? [M/F] ')).strip().upper()[0]

while sex not in 'FFMMffmm':
    sex = str(input('Sexo inválido! Por favor, informe seu sexo? [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sex))