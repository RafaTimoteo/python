#Alistamento militar

from datetime import date

nascimento = int(input('Qual seu ano de nascimento? '))
ano = date.today().year
idade = (ano - nascimento)
alistamento = nascimento + 18


if idade > 18:
    print('Nesse ano, voce completa (ou já completou) {} anos, seu ano de alistamento foi {}, possui {} anos de atrasado.'.format(idade, alistamento, (ano-alistamento)))
elif idade < 18:
    print('Nesse ano, voce completa (ou já completou) {} anos, seu ano de alistamento será {}, faltam {} anos.'.format(idade, alistamento, (alistamento-ano)))
else:
    print('Nesse ano, voce completa (ou já completou) {} anos, logo, deverá se alistar no presente ano.'.format(idade))
