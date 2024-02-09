from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*18)
print('Vou pensar entre um numero de 0 a 5. Tente adivinhar...')
print('-=-'*18)
jogador = int(input('Em que numero eu pensei....? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens acertou!')
else:
    print('Que pena! Errou! Pensei {}'.format(computador))