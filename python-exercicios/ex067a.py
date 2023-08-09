# Tabuada (while + for)

n = 1
r = 0

while True:
    print('-=-'*25)
    n = int(input('Digite um valor para saber a sua tabuada [n negativo encerra]: '))
    print('-=-'*25)
    if n > 0:
        for x in range(1, 11):
            r = n * x
            print(f'{n} x {x} = {r}')
    else:
        break

print('Programa de tabuada encerrado, volte sempre!')
print('-=-'*25)