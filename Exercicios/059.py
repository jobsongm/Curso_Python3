n1 = int(input('Digite primeiro valor: '))
n2 = int(input('Digite segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa]''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opcao == 2:
        multiplica = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplica}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Informe primeiro numero: '))
        n2 = int(input('Informe segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente!')
print('Fim do programa!')