# Tabuada (while + while)

n = 1
r = 0

while True:
    print('-=-'*25)
    n = int(input('Digite um valor para saber a sua tabuada [n negativo encerra]: '))
    print('-=-'*25)
    if n > 0:
        x = 1
        while x <= 10:
            r = n + x
            print(f'{n} x {x} = {r}')
            x = x + 1
    else:
        break

print('Programa de tabuada encerrado, volte sempre!')
print('-=-'*25)