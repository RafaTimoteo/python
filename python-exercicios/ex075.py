pares = []
num9 = 0
numeros = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite um último valor: ')))

print('\n')

print(f'Foram digitados os valores: {numeros}')

print('-=-'*15)
if 9 in numeros:
    print(f'O numero 9 apareceu {numeros.count(9)} vezes')
else:
    print('Nào houve número 9')
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('Não houve número 3')
for n in numeros:
    if n % 
        print(f'Números pares: {pares}')
    else:
        print('Não houve números pares')
print('-=-'*15)