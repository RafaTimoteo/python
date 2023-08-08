# Varios valores

count = 0
num = 0
sun = 0

print('-=-'*20)
print('Os números seram somados entre si, digite 999 para parar')
print('-=-'*20)

while num != 999:    
    num = int(input('Digite um numero: '))
    if num != 999:
        sun = sun + num
        count = count + 1
    else:   
        print('-=-'*20)
        print('Fim do programa!')

print('-=-'*20)
print('Foram digitados {} números e a soma entre eles é {}'.format(count, sun))
print('-=-'*20)
