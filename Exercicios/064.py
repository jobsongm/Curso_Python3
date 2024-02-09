count = soma = num = 0
num = int(input('Digite um numero! [999 para parar] '))
while num != 999:
    count += 1
    soma += num
    num = int(input('Digite um numero! [999 para parar] '))
print('Acabou')
print('Foram digitados {} e a soma entre eles foram {}'.format(count,soma))
