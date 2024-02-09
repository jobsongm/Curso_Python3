primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de PA: '))
termo = primeiro
total = 0
cont = 1
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você que a mais? '))
print('Fim')