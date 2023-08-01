#Progressão aritmética

print('-=-'*15)
print('PROGRESSÃO ARITMÉTICA')
print('-=-'*15)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progreção: '))
f = p + (10 - 1) * r

for c in range(p, f, r):
    print(c, end=' > ')
print('Acabou') 