
old_man = 0
woman = 0
man = 0
woman_sub20 = 0
sun_age = 0


for c in range(1, 5):
    name = str(input('Qual é o nome da {}º pessoa: '.format(c))).strip().capitalize()
    age = int(input('Qual é a idade da {}º pessoa: '.format(c)))
    sex = str(input('Qual é o sexo da {}º pessoa (masculino/feminino): '.format(c))).strip().lower()

    print('')

    if sex == 'masculino':
        man = man + 1
        sun_age = sun_age + age
        if age > old_man:
            old_man = age
            name_old_man = name

    elif sex == 'feminino':
        woman = woman + 1
        sun_age = sun_age + age
        if age < 20:
            woman_sub20 = woman_sub20 + 1
   
    else:
        print('OPÇÃO DE SEXO INVÁLIDA!')
        print(' ')
        exit()

print('-=-'*20)

print('A idade média é: {}'.format(sun_age/4))

print('-=-'*20)

print('{} pessoas são mulheres'.format(woman))
print('Dessas, {} estão abaixo dos 20 anos'.format(woman_sub20))

print('-=-'*20)

print('{} pessoas são homens'.format(man))
print('Desses, o {} é o mais velho com {} anos de idade'.format(name_old_man, old_man))

print('-=-'*20)
