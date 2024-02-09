num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para Binario')
print('[ 2 ] Converter para Octal')
print('[ 3 ] Converter para Hexadecimal')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('{} convertido para binario é {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido pra Octal é {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida!')