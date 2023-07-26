#Calculando a tangente de um angulo

import math

angulo = float(input('Digite o valro de um ângulo: '))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O seno desse angulo é {:.2f};'.format(seno))
print('O cosseno desse angulo é {:.2f};'.format(cos))
print('A tangente desse angulo é {:.2f}.'.format(tan))