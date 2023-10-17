from random import randint
import random
from time import sleep
lista = list()
jogos = list()
print('*'*40)
print('    NÚMEROS MAIS SORTEADOS NA MEGA SENA    ')
print('*'*40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    cont = 0
    while True:
        num = [53, 10, 5, 42, 37, 33, 4, 23, 27, 30, 28,
               41, 57, 34, 11, 16, 29, 35, 44, 17, 43, 51,
               24, 32, 49, 38, 2, 36, 13, 56, 6, 8, 52,  46]
        num = random.sample(num, 1)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-='*3, f'SORTEANDO {quant} JOGOS ', '-='*3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, 'BOA SORTE! >', '-='*3)
print()
print('*'*45)


print()

while True:
    n= int(input('''digite o valor que quer consultar ou
"0" para sair:
"99" para os números mais azarados:
"88" para os números mais sorteados:
Sua escolha: '''))
    print() 

    if n ==53: 
        print(f'O número {n} saiu 283 vezes')
    elif n ==10: 
        print(f'O número {n} saiu 280 vezes')
    elif n ==5: 
        print(f'O número {n} saiu 269 vezes')
    elif n ==42: 
        print(f'O número {n} saiu 269 vezes')
    elif n ==37: 
        print(f'O número {n} saiu 268 vezes')
    elif n ==33: 
        print(f'O número {n} saiu 265 vezes')
    elif n ==23: 
        print(f'O número {n} saiu 263 vezes')
    elif n ==27: 
        print(f'O número {n} saiu 261 vezes')
    elif n ==30: 
        print(f'O número {n} saiu 260 vezes')
    elif n ==28: 
        print(f'O número {n} saiu 260 vezes')
    elif n == 41: 
        print(f'O número {n} saiu 260 vezes')
    elif n ==54: 
        print(f'O número {n} saiu 259 vezes')
    elif n ==34: 
        print(f'O número {n} saiu 260 vezes')
    elif n ==11: 
        print(f'O número {n} saiu 258 vezes')
    elif n ==16: 
        print(f'O número {n} saiu 258 vezes')
    elif n ==29: 
        print(f'O número {n} saiu 258 vezes')
    elif n ==35: 
        print(f'O número {n} saiu 258 vezes')
    elif n ==44: 
        print(f'O número {n} saiu 258 vezes')
    elif n ==17: 
        print(f'O número {n} saiu 257 vezes')
    elif n ==43: 
        print(f'O número {n} saiu 257 vezes')
    elif n ==51: 
        print(f'O número {n} saiu 257 vezes')
    elif n ==24: 
        print(f'O número {n} saiu 256 vezes')
    elif n ==32: 
        print(f'O número {n} saiu 254 vezes')
    elif n ==49: 
        print(f'O número {n} saiu 254 vezes')
    elif n ==38: 
        print(f'O número {n} saiu 253 vezes')
    elif n ==2: 
        print(f'O número {n} saiu 252 vezes')
    elif n ==36: 
        print(f'O número {n} saiu 252 vezes')
    elif n ==13: 
        print(f'O número {n} saiu 251 vezes')
    elif n ==56: 
        print(f'O número {n} saiu 251 vezes')
    elif n ==6: 
        print(f'O número {n} saiu 249 vezes')
    elif n ==8: 
        print(f'O número {n} saiu 249 vezes')
    elif n ==52: 
        print(f'O número {n} saiu 248 vezes')
    elif n ==46: 
        print(f'O número {n} saiu 246 vezes')
    elif n ==18: 
        print(f'O número {n} saiu 242 vezes')
    elif n ==50: 
        print(f'O número {n} saiu 242 vezes')
    elif n ==58: 
        print(f'O número {n} saiu 239 vezes')
    elif n ==50: 
        print(f'O número {n} saiu 240 vezes')
    elif n ==12: 
        print(f'O número {n} saiu 239 vezes')
    elif n ==1: 
        print(f'O número {n} saiu 237 vezes')
    elif n ==20: 
        print(f'O número {n} saiu 237 vezes')
    elif n ==45: 
        print(f'O número {n} saiu 237 vezes')
    elif n ==47: 
        print(f'O número {n} saiu 237 vezes')
    elif n ==25: 
        print(f'O número {n} saiu 236 vezes')
    elif n ==40: 
        print(f'O número {n} saiu 236 vezes')
    elif n ==7: 
        print(f'O número {n} saiu 235 vezes')
    elif n ==19: 
        print(f'O número {n} saiu 234 vezes')
    elif n ==31: 
        print(f'O número {n} saiu 233 vezes')
    elif n ==39: 
        print(f'O número {n} saiu 233 vezes')
    elif n ==39: 
        print(f'O número {n} saiu 233 vezes')
    elif n ==59: 
        print(f'O número {n} saiu 233 vezes')
    elif n ==60: 
        print(f'O número {n} saiu 233 vezes')
    elif n ==9: 
        print(f'O número {n} saiu 232 vezes')
    elif n ==14: 
        print(f'O número {n} saiu 232 vezes')
    elif n ==3: 
        print(f'O número {n} saiu 227 vezes')
    elif n ==48: 
        print(f'O número {n} saiu 227 vezes')
    elif n ==15: 
        print(f'O número {n} saiu 217 vezes')
    elif n ==22: 
        print(f'O número {n} saiu 216 vezes')
    elif n ==21: 
        print(f'O número {n} saiu 212 vezes')
    elif n ==55: 
        print(f'O número {n} saiu 207 vezes')
    elif n ==23: 
        print(f'O número {n} saiu 205 vezes')
    
    elif n == 99:
        print('10 números mais azarados:')
        print('23, 55, 21, 22, 15, 48, 3, 14, 60, 39')
    elif n == 88:
        print('''Os dez números mais sorteados:
[53, 10, 05, 42, 37, 33, 04, 23, 27, 30]''')
   
    
    elif n == 0:
        break
    print()

            
listagem = ('53', 283 ,
            '10', 280,
            '05', 269,
            '42', 269,
            '37', 268,
            '33', 265,
            '04', 264,
            '23', 263,
            '27', 261,
            '30', 260,
            '28', 260,
            '41', 260,
            '54', 259,
            '34', 260,
            '11', 258,
            '16', 258,
            '29', 258,
            '35', 258,
            '44', 258,
            '17', 257,
            '43', 257,
            '51', 257,
            '24', 256,
            '32', 254,
            '49', 254,
            '38', 253,
            '02', 252,
            '36', 252,
            '13', 251,
            '56', 251,
            '06', 249,
            '08', 249,
            '52', 248,
            '46', 246,)
                
print('-'*40)
print(f'{"NÚMEROS MAIS SORTEADOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2==0:
        print(f'{listagem[pos]:.<15}', end='')
    else:
        print(f'Saiu: {listagem[pos]:>5.0f} vezes')
        
print('-'*40)
