import math
angulo = float(input('Digite o angolo: '))
seno = math.sin(math.radians(angulo))
print('O angulo {} tem o  seno de  {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo {} tem o  cosseno de  {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem o  tangente de  {:.2f}'.format(angulo,tangente))