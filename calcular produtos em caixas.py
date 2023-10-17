from time import sleep
print('')
print('-=-'*15)
print('__Valor dos produtos unitários__')
print('')
print('-=-'*15)

total = float(input('Qual o valor total dos produtos? '))
cx = int(input('Quantas caixas vieram? '))
pcx = int(input('Quantos produtos vem em cada caixa? '))

tot = total/ (cx*pcx)



print('')
print('Calculando...')
sleep(1.5)
print('-=-'*15)
print(f'Um total de {cx*pcx} produtos, cada produto individual custa {tot:.2f}')
print('-=-'*15)


