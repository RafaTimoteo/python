# Soma dos valores

sun = c = n = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    else:
        sun = sun + n
        c = c + 1

print(f'A soma dos {c} termos vale {sun}')