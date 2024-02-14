cont = ('zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
while True:
    num = int(input('Digite um numero entre 0 a 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente. ',end='')
print(f'Você digitou {cont[num]}')