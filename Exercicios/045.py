from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
print('''Sua opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua escolha? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador escolheu {}'.format(itens[jogador]))
if pc == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador Vence')
    else:
        print('Jogada invalida!')
elif pc == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada invalida!')
elif pc == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada invalida!')
