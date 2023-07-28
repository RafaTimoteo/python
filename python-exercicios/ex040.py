#media de notas com estrutura de condição

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

if m >= 7.0:
    print('APROVADO. Sua média foi {:.1f}'.format(m))
elif m >= 5.0:
    print('RECUPERAÇÃO. Sua média foi {:.1f}'.format(m))
elif m < 5.0:
    print('REPROVADO. Sua média foi {:.1f}'.format(m))