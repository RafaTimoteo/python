#Pintura de parede#
b = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = float((b*h))
print('Sua parede tem a dimensão de {:.1f}x{:.1f}, uma área de {:.1f}m²'.format(b, h, a))
print('Para pinta-la, será necessário {:.1f}L de tinta'.format(a/2))
