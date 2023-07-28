#Nadadores por idade

from datetime import date

nascimento = int(input('Em que ano o atleta nasceu? '))
idade = (date.today().year) - nascimento

if idade <= 9.0:
    print('O atleta tem {} anos, portanto, faz parte da categoria MIRIM.'.format(idade))
elif idade > 9.0 and idade <= 14.0:
    print('O atleta tem {} anos, portanto, faz parte da categoria INFANTIL.'.format(idade))
elif idade > 14.0 and idade <= 19.0:
    print('O atleta tem {} anos, portanto, faz parte da categoria JUNIOR.'.format(idade))
elif idade > 19.0 and idade <= 20.0:
    print('O atleta tem {} anos, portanto, faz parte da categoria SENIOR.'.format(idade))
else:
    print('O atleta tem {} anos, portanto, faz parte da categoria MASTER.'.format(idade))
    
    
