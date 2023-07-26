#numero par ou impar

num = int(input('Digite um número inteiro qualquer: '))

# print('O número {} é par'.format(num) if num % 2 == 0 else 'O número {} é ímpar'.format(num))

if num % 2 == 0:
     print('O número {} é par'.format(num))
else:
     print('O número {} é ímpar'.format(num))
