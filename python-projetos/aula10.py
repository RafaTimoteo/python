n1 = float(input('Digite a primeira nota: '))
n2 = float(input('DIgite a segunda nota: '))

m = (n1+n2)/2
print('Sua média foi: {}'.format(m))

# if m >= 6.00:
#     print('Está acima da média. PARABENS!')
# else:
#     print('Está abaixo da média. ESTUDE MAIS!')    

print('Está acima da média. PARABENS!' if m >= 6.00 else 'Está abaixo da média. ESTUDE MAIS!')