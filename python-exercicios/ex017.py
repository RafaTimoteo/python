#Calculando a Hipotenusa

'''from math import sqrt

cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input('Digite o comprimento do catetro adjacente: '))

h = sqrt((cat_o**2)+(cat_a**2))

print('O comprimento da  hipotenusa de um triangulo com catetos {} e {} é igual a:  {:.2f}.'.format(cat_o, cat_a, h))'''

from math import hypot

cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input('Digite o comprimento do catetro adjacente: '))
h = hypot(cat_o, cat_a)
print('O comprimento da  hipotenusa de um triangulo com catetos {} e {} é igual a:  {:.1f}.'.format(cat_o, cat_a, h))
