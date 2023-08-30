# Adicionando valores a uma lista e exibindo em ordem crescente

choice = 'S'
valores = list()
print('-=-'*15)
while True:
    c = None
    if choice == 'S':
        c = int(input('Digite um valor: '))
        if c in valores:
            print('Valor duplicado, não vou adicionar!')
        elif c == ' ':
            print('Tente novamente!')
        else:
            valores.append(c)
            print('valor adicionado com sucesso!')
        print('-=-'*15)
        choice = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        while choice != 'S' and choice != 'N':
            choice = str(input('Opção inválida! Tente novamente \nQuer continuar? [S/N] ')).upper().strip()[0]
    elif choice == 'N':
        break

print('-=-'*15)
print(f'Foram digitados os valores: {sorted(valores)}')
