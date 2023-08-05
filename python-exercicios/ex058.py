#Tente adivinhar (com while)

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número de 0 a 10...')
print('-=-' * 20)

num = randint(0,10)
chute = int(input('Qual número eu pensei: '))
count = 0

print('PROCESSANDO...')
sleep(1)

while num != chute:
    count = count + 1
    chute = int(input('Voce errou! Tente novamente: '))
    sleep(1)

print('Acertou mizeravi! Pensei no número {} mesmo. Conseguiu na {}º tentativa'.format(num, count))