km = float(input('Digite a km: '))
if km <= 200:
    p1 = km*0.50
    print('Passagem custa! R${:.2f}'.format(p1))
else:
    p2 = km*0.45
    print('Passagem custa! R${:.2f}'.format(p2))