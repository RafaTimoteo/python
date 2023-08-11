# Análise de produtos (nao esta resolvido)

totvalor = prod_upk = count = menor = 0
nome_menor = ' '
choice = 'S'

while True:
        print('-=-'*15)
        nome = str(input('Digite o nome do produto: ')).strip().capitalize()
        valor = float(input('Digite o valor: '))
        print('-=-'*15)
        count += 1
        totvalor += valor

        if count == 1:
            menor = valor
            nome_menor = nome

        else:
            if valor < menor:
                menor = valor
                nome_menor = nome

        if valor > 1000:
            prod_upk += 1

        choice = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        while choice != 'S' and choice != 'N':
            choice = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if choice == 'N':
             print('Fim do programa!')
             break

print('-=-'*15)
print(f'Total gasto R${totvalor:.2f}')   
print(f'Ao total, {prod_upk} produtos custa mais de R$1000,00')
print(f'O produto mais barato foi {nome_menor}')
print('-=-'*15)
