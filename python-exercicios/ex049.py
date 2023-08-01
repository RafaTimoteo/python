#Tabuada com for

n = int(input('Dgite um número inteiro '))

print('-'*15)

for c in range(1,11):
    print('{} x {} = {}'.format(n, c, (n*c)))

print('-'*15)        