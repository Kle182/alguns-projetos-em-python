print('-=-=-Teste de IMC-=-=-')
print('')
from time import sleep
nome = input('Qual o seu nome? ')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
res = (peso / altura**2)
print('Seu IMC é igual a:{:.1f}'.format(res))
print('-=-'*20)
print('...Processando...')
sleep(1)
print('...Processando...')
sleep(1)
print('...Processando...')
sleep(1)
print('-=-'*20)
if altura >= 2.00:
    print('Só par constar {} tu é grande em girafão!'.format(nome))
if altura <=1.49:
    print('Caracas {}, você esqueceu de crescer foi!'.format(nome))
if res<18.5:
    print(nome, 'Você está abaixo de peso, vai comer miseravi')
if res>18.5 and res<=26:
    print(nome, 'Seu peso está normal Parabéns')
if res>=26.1 and res<29.9:
    print(nome, 'Está com sobre peso, está na hora de uma dieta hein!')
if res>30 and res <34.9:
    print(nome, 'Você está com obesidade grau 1, resumindo gordinho')
if res >35 and res<39.9:
    print(nome, 'Cuidado você está com obesidade grau 2, resumindo gordão')
if res >40:
    print(nome, 'Pode encomendar o caixão vc esta mórbido!')
print('-=-'*20)
if altura >= 1.50 and altura < 1.57:
    print('Seu peso ideal é de: 49 a 55 Kg')
if altura >= 1.57 and altura < 1.64:
    print('Seu peso ideal é de: 52 a 59 Kg')
if altura >= 1.64 and altura < 1.65:
    print('Seu peso ideal é de: 54 a 62 Kg')
if altura >= 1.65 and altura < 1.69:
    print('Seu peso ideal é de: 57 a 67 Kg')
if altura >= 1.69 and altura < 1.71:
    print('Seu peso ideal é de: 63 a 76 Kg')
if altura >= 1.71 and altura < 1.74:
    print('Seu peso ideal é de: 66 a 79 Kg')
if altura >= 1.74 and altura < 1.75:
    print('Seu peso ideal é de: 68 a 80 Kg')
if altura >= 1.76 and altura < 1.79:
    print('Seu peso ideal é de: 70 a 84 Kg')
if altura >= 1.79 and altura < 1.81:
    print('Seu peso ideal é de: 72 a 82 Kg')
if altura >= 1.81 and altura < 1.84:
    print('Seu peso ideal é de: 75 a 91 Kg')
if altura >= 1.84 and altura < 1.86:
    print('Seu peso ideal é de: 77 a 95 Kg')
if altura >= 1.86 and altura < 1.89:
    print('Seu peso ideal é de: 79 a 98 Kg')
if altura >= 1.89 and altura < 1.92:
    print('Seu peso ideal é de: 82 a 102 Kg')
if altura >= 1.92 and altura <= 1.98:
    print('Seu peso ideal é de: 84 a 106 Kg')
    
    

