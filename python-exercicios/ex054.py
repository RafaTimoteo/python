#Maiores de idade

from datetime import date

today = date.today().year
over = 0
under = 0

for pess in range(1, 8):
    born = int(input('Digite um ano de nascimento da {}º pessoa: '.format(pess)))
    age = today - born
    if age >= 18:
        over = over + 1
    else:
        under = under + 1

print('{} pessoas são maiores de 18 anos'.format(over))
print('{} pessoas são menores de 18 anos'.format(under))