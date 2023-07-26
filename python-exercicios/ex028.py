#Tente adivinhar

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5...')
print('-=-' * 20)

num = randint(0,5)
chute = int(input('Qual número eu pensei: '))
print('PROCESSANDO...')
sleep(2)

if num == chute:
    print('Acertou mizeravi! tinha pensado no número {} mesmo'.format(num))
else:
    print('Voce errou! O numero que eu tinha pensado era {} e não {}'.format(num, chute))    