#joquempo

from random import randint

print('''Escolha uma das opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
itens = ('Pedra', 'Papel', 'Tesoura')

user = int(input('Digite sua escolha: '))
pc = randint(0, 2)

if user <= 2 and user >= 0:
    
    if user == 0:
        if pc == 0:
            print('Empate')
        elif pc == 1: 
            print('O Computador ganhou')
        else:
            print('Voce ganhou')

    elif user == 1:
        if pc == 0:
            print('Voce ganhou')
        elif pc == 1:
            print('Empate')
        else:
            print('O Computador ganhou')

    else:
        if pc == 0:
            print('O Computador ganhou')
        elif pc == 1:
            print('Voce ganhou')
        else:
            print('Empate')

    print('-=-'*12)     
    print('O computador escolheu {}'.format(itens[pc]))
    print('Voce escolheu {}'.format(itens[user]))
    print('-=-'*12)   
      
else:
    print('Opção inválida!')
