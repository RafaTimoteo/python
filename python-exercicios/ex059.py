

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
choice = 0

print('-=-'*15)

while choice != 5:
    print('''        O que deseja fazer?
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos Números
        [ 5 ] Sair do Programa''')
    choice = int(input('        Sua escolha: '))

    print('-=-'*15)

    if choice == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
    elif choice == 2:
        print('{} x {} = {}'.format(n1, n2, (n1*n2)))
    elif choice == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O {} é maior que o {}'.format(n2, n1))
        else:
            print('Os dois valores são iguais')
    if choice == 4:
        print('Digite novos valores')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif choice > 5:
        print('Opção inválida, tente novamente')

    print('-=-'*15)