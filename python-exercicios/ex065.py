# Média e maior e menor de vários valores

n = 0
maior = n
menor = 0
count = 0
soma = 0
choice = 'S'

while choice in 'Ss':
    print('-=-'*20)
    n = int(input('Digite um número: '))

    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    
    soma = soma + n
    count = count + 1
    print('-=-'*20)
    choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma / count

print('-=-'*20)
print('Foram digitados {} valores'.format(count))
print('A soma entre eles é {}'.format(soma))
print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))
print('A média entre os valores foi {:.1f}'.format(media))
print('-=-'*20)