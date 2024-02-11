soma = count = 0
while True:
    num = int(input('Digite um valor! [Digite 999 para parar] '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Foram digitados {count} A soma dos valores foi {soma}')