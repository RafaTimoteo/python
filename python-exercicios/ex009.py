#Tabuada#
n = int(input('Dgite um número inteiro '))
x = int(0)
print('-'*15)
while (x <= 10):
    print('{} x {:2} = {}'.format(n, x, (n*x)))
    x = x + 1
    print('-'*15)        