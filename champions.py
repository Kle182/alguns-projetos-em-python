import pygame
pygame.init()
pygame.mixer.music.load('musicachampions.mp3')
pygame.mixer.music.play()
pygame.event.wait()

from random import randint
from time import sleep
print('')
print('___Champions 2022___')
print('')
print('Quartas de Final')
print('Em instante a bola vai rolar')
sleep(2)
print('')
print('-='*15)
print('----GRUPO A----')
print('-='*15)


real = randint(0, 5)
psg = randint(0, 5)
print(f'Real Madrid {real}X{psg} PSG ')
sleep(2)
print('')
if real>psg:
    v1= 'Real Madrid'    
    print('Real ganhou')
elif psg> real:
    v1= 'PSG'     
    print('PSG ganhou')
elif real==psg:
    sleep(3)
    print('Empate')
    preal = randint(0, 10)
    ppsg = randint(0, 10)
    print(f'Nos penaltis Real Madrid {preal}X{ppsg} PSG ')
    if preal>ppsg:
        v1= 'Real Madrid'    
        print('Real ganhou')
    elif ppsg> preal:
        v1= 'PSG'     
        print('PSG ganhou')
sleep(3)        

print('')
print('**'*15)
mc = randint(0, 5)
mu = randint(0, 5)

print(f'City {mc}X{mu} United ')
sleep(2)
if mc>mu:
    v2= 'City'
    print('City ganhou')
elif mu> mc:
    v2= 'United'
    print('United ganhou')
elif mc==mu:
    print('Empate')
    sleep(2)
    pmc = randint(0, 10)
    pmu = randint(0, 10)
    print(f'Nos penaltis City {pmc}X{pmu} United ')
    if pmc>pmu:
        v2= 'City'
        print('City ganhou')
    elif pmu> pmc:
        v2= 'United'
        print('United ganhou')
print('')
print('Agora vamos para o grupo B')

sleep(4) 
print('**'*15)
print('----GRUPO B----')
print('**'*15)

print('')
print('**'*15)
barca = randint(0, 5)
bayer = randint(0, 5)

print(f'Barça {barca}X{bayer} Bayer ')
sleep(2)
if barca>bayer:
    v3='Barça'
    print('Barça ganhou')
elif bayer> barca:
    v3='Bayer'
    print('Bayer ganhou')
elif barca==bayer:
    sleep(2)
    print('Empate')
    sleep(2)
    pbarca = randint(0, 10)
    pbayer = randint(0, 10)
    print(f'Nos penaltis Barça {pbarca}X{pbayer} Bayer ')
    if pbarca>pbayer:
        v3='Barça'
        print('Barça ganhou')
    elif pbayer> pbarca:
        v3= 'Bayer'
        print('Bayer ganhou')

sleep(3) 
print('')
print('**'*15)
liver = randint(0, 5)
boru = randint(0, 5)

print(f'Liver {liver}X{boru} Borucia ')
sleep(2)
if liver>boru:
    v4= 'Liver'
    print('Liver ganhou')
    
elif boru> liver:
    v4= 'Boru'
    print('Boru ganhou')
elif liver==boru:
    sleep(2)
    print('Empate')
    sleep(2)
    pliver = randint(0, 10)
    pboru = randint(0, 10)
    print(f'Nos penaltis Liver {pliver}X{pboru} Borucia ')
    if pliver>pboru:
        v4= 'Liver'
        print('Liver ganhou')
    elif pboru> pliver:
        v4= 'Boru'
        print('Boru ganhou')
print('')
print('preparando semi final')
sleep(3) 
        
print('')
print('**'*15)
print('---SEMI FINAL---')
print('')
semi1= randint(0, 5)
semi2= randint(0, 5)
print('{} {}x{} {}'.format(v1, semi1, semi2, v2))
sleep(2)
if semi1> semi2:
    final1= v1
    print(f'{v1} Ganhou')
elif semi2> semi1:
    final1= v2
    print(f'{v2} Ganhou')
elif semi1==semi2:
    sleep(2)
    print('Empate')
    sleep(2)
    psemi1= randint(0, 9)
    psemi2= randint(0, 9)
    print(f'Nos penaltis {v1} {psemi1} x {psemi2} {v2}')
    if psemi1 > psemi2:
        final1=v1
        print(f'{v1} venceu')
    elif psemi2>psemi1:
        final1= v2
        print(f'{v2} venceu')
sleep(4) 

print('')
semi3= randint(0, 5)
semi4= randint(0, 5)
print('{} {}x{} {}'.format(v3, semi3, semi4, v4))
sleep(2)
if semi3> semi4:
    final2= v3
    print(f'{v3} Ganhou')
elif semi4> semi3:
    final2= v4
    print(f'{v4} Ganhou')
elif semi3==semi4:
    sleep(2)
    print('Empate')
    sleep(2)
    psemi3= randint(0, 9)
    psemi4= randint(0, 9)
    print(f'Nos penaltis {v3} {psemi3} x {psemi4} {v4}')
    if psemi3>psemi4:
        final2= v3
        print(f'{v3} {psemi3} X {psemi4} {v4}')
        print(f'{v3} ganhou')
    elif psemi4> psemi3:
        final2= v4
        print(f'{v3} {psemi3} X {psemi4} {v4}')
        print(f'{v4} ganhou')
print('')
print('**'*15)
print('---GRANDE FINAL---')
print('')

print(f'{final1} x {final2}')

print('Em instante a grande final...')
sleep(3)
z1= randint(0, 5)
z2= randint(0, 5)
print('Bola rolando')
sleep(1)
print('Haja coração....')
sleep(2)
print(f'{final1} {z1} x {z2} {final2}')
sleep(2)
print('')
if z1>z2:
    print(f'O grande campeão foi: "{final1}" com um placar de {z1} a {z2}')
    print('')
    print(f'PARABÉNS {final1}')
elif z2>z1:
    print(f'O grande campeão foi "{final2}" com um placar de {z2} a {z1}')
    print('')
    print(f'PARABÉNS {final2}')
elif z1==z2:
    print('Empate')
    sleep(2)
    pf1= randint(0, 9)
    pf2 = randint(0, 9)
    if pf1> pf2:
        print(f'Nos penaltis grande campeão foi: "{final1}" com um placar de {f1} a {pf2} nos penaltis')
        print(f'Parabéns {final1}')
    elif pf2 > pf1:
        print(f'Nos penaltis grande campeão foi: "{final2}" com um placar de {pf2} a {pf1}')
        print(f'Parabéns {final2} é o grande campeão')
print('____Até a próxima temporada____')







