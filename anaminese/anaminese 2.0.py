from datetime import date
nome = []
idade = []
queixa = []
def linha():
    print('--'*20)
while True:
    
    nome.append(str(input('Qual o nome: ')))
    linha()
    idade.append(int(input('Idade: ')))
    linha()
    queixa.append(str(input('Qual a sua principal queixa: ')))
    linha()
    obs = str(input('Observações: '))
    print('*'*30)
    print(f'o paciente {nome[0]}, idade de  {idade[0]} anos se queixa de {queixa[0]}')
    print('*'*30)
    linha()
    print()
    r = str(input('Gerar relatório automatizado? [S/N] ')).strip().upper()[0]
    if r == 'S':
        break
    

print()
from time import sleep
print('-=-'*15)
print('ESCOLHA AUTOMATIZADA DE PONTOS')
print('')
n = (nome[0])
i = (idade[0])
q = (queixa[0])
print('')
print('''Qual a sua principal queixa:
[1] Sinusite:
[2] dor lombar:
[3] dor cervical:
[4] dor pernas:
[5] dor joelhos:
[6] ansiedade:
[7] zumbido no ouvido:
[8] Protocolo de AVC:
[9] Mandibula e boca
[10] enxaqueca''')
opcao = int(input('Sua opção: '))
print('')
print('-=-=-Gerando Diagnóstico-=-=-')
print('..')
sleep (0.8)
print('....')
sleep (0.7)

print('-=-=Diagnóstico Gerado com sucesso-=-=')
print()
if opcao==1:
    print('Para Sinusite os pontos mais indicados são:\nig4:\nig11:\nyintang:\nIG20:\nIG14:\nVG23:\nE5:\npode-se usar moxa para eles! ')
elif opcao==2:
    print('Para dores lombares os ponto indicados são:\nR3:\nR6:\nB23:\nb62:\nB64:\nVB24:\nID33:\nBP3:\nB52:\nB40:\n pode-se fazer uso de moxa e ventosa para a região lombar! ')
elif opcao==3:
    print('Para dores cervicais os pontos indicados são:\nID1:\nID3:\nTA1:\nTA3\nIG1:\nIg4:\nIG15:\nVB13\nIG14\nEsse é o tratamneto pelo tendino muscular!')
elif opcao==4:
    print('Para dores nas pernas os pontos indicados são: \nF3:\nF8:\nR7:\nE38:\nB62:\nE36:\nE34')
elif opcao==5:
    print('Para dores nos joelhos os pontos indicados são: \nF3:\nF8:\nR7:\nVB41:\nF8:\n36:\n34:\nE35:\nXiyang:\nMoxa é uma ótima opção para esse tratamento')
elif opcao==6:
    print('Para ansiedade existe diversos tipos de tratamentos:\nChikong com 5 agulhas é ótimo:\nIg4 com yintang e VG20')
elif opcao==7:
    print('Para zumbido os pontos indicados sao: IG4:\nIG5:\nR3:\nR7:\nP8:')
elif opcao==8:
    print('Para pós AVC utiliza-se:\n VG26: \nVG26: \nBP6:\nC1:\nB40:\nVB33:\nVB39:\nP9:\nVB20:\nutiiliza-se cranio-acupuntura para AVC.')
elif opcao==9:
    print('Para  mandibula e boca utiliza-se:\nE6: \nE7: \nTA21:\nTA17:\nID18:\nIG4: ')

    
else:
    opcao==10
    print('''local da dor de cabeça:
    [1] Frontal:
    [2] Lateral:
    [3] atras da cabeça:''')
    local = int(input('Selecione uma opção:'))
    if local==1:
        print('Para dores de cabeça frontal utiliza-se:\nIG4:\nE44:\nYintang:\n pode ser usado cone chines')
    elif local==2:
        print('Para dor de cabeça lateral utiliza-se:\nTA5:\nVB41:\nYintang:\n pode ser usado cone chines')
    elif local==3:
        print('Para dor de cabeça na nuca utiliza-se:\nID3:\nB62:\npode ser usado cone chines')
print('')  
print('-=-'*15)      
print(f'Tratamento gerado para {n} que tem {i} anos de idade com queixa de {q}')
print('-=-'*15)
        
    
if idade[0]>40 or idade[0]<49:
    print('Acupuntura é um ótimo meio de tratar sua saúde! ')
print('')
if idade[0]>50:
    print('Sempre fortaleça o YIN de pessoas com mais de 50 anos')
if idade[0]>30:
    print('Sempre se alimente com comida saudavel') 

print()
a = (date.today())
b=(str(a).split())

fileName = (n)
fileName = fileName + '.txt'
arq = open(fileName, 'a')
arq.write(f'Data: {b[0][8:10]}/{b[0][5:7]}/{b[0][0:4]}\n')
arq.write(f'Paciente - {n}\n')
arq.write(f'Idade - {i}\n')
arq.write(f'Queixa - {q}\n')
arq.write(f'Tratamento escolhido- {opcao}\n')
print('')
arq.write(f'Obs: {obs}\n')
arq.write('********************* \n')
arq.close()





