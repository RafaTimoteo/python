#sorteio de alunos

from random import choice

al1 = str(input('Digite o nome de um aluno: '))
al2 = str(input('Digite o nome de outro aluno: '))
al3 = str(input('Digite o nome de outro aluno: '))
al4 = str(input('Digite o nome do último aluno: '))

lista = [al1, al2, al3, al4]

print('O nome escolhido é {}.'.format(choice(lista)))