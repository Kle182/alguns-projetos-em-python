from time import sleep
from datetime import date
import datetime
from random import randint
real = randint(0,9999)
print('____TRANSFERENCIA____')
print('*'*30)
print()
d = str(input('De quem saira o produto: '))
mes = str(input('Para quem sera a transferencia: '))
p= list()
r= list()
soma=0
while True:
    p.append(input('produto: '))
    p.append (int(input('quantas unidades: ')))
    p.append(float(input('Valor: ')))
    r.append(p[:])
    p.clear()
    resp= str(input('Acrescentar mais ou finalizar [A/F]')).strip().upper()[0]
    if resp=='F':
        break
print()
a = (date.today())
b=(str(a).split())


fileName = (f'{b[0][8:10]}{b[0][5:7]}{b[0][0:4]}')
fileName = fileName + '.txt'
arq1 = open(fileName, 'w')
#cabeçario
arq1.write(f'Nº{real}   ')
arq1.write(f'Data: {b[0][8:10]}/{b[0][5:7]}/{b[0][0:4]}\n')
arq1.write('\n')
arq1.write('_______TRANSFERÊNCIA________\n')
arq1.write('\n')
arq1.write(f'De: {d} / {mes}\n')
arq1.write('____________________________\n')

for x in r:
    rr=(x[1]*x[2])
    print(f'{x[0]} {x[1]} unidades')
    print(f'valor unitário R${x[2]} total R${rr:.2f}')
    soma+=rr
    print('________________________________________')
    
    arq1.write(f'{x[0]} {x[1]} unidades\n')
    arq1.write(f'R${x[2]} total {x[1]*x[2]:.2f}\n')
    arq1.write('____________________________\n')
    arq1.write('\n')

arq1.write(f'TOTAL--------------R${soma:.2f}')
print(f'Total______{soma:.2f}')


arq1.close() 




    
