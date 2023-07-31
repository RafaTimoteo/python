
f = int(input('Quantos números deseja somar? '))
s = 0

for c in range(1, f+1):
    num = int(input('Digite um número: '))
    s = s + num
print('A soma dos valores é igual a {}'.format(s))