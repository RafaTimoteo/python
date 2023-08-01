#Soma de números ímpares

s = 0
count = 0

for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 1:
        s = s + num
        count = count + 1

print('Foram digitados {} números ímpares e  a soma entre eles é igual a  {}'.format(count, s))