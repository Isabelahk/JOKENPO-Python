from random import randint
from time import sleep
itens = ('Nada', 'Pedra', 'Papel', 'Tesoura')
computador = randint(1,3)

print('''
=================================
        Suas opções:
    [1] Pedra.
    [2] Papel.
    [3] Tesoura.
=================================
''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 11)

print('Computador jogou {}'.format(itens[computador]))

print('Você jogou {}'.format(itens[jogador]))

print('-=' * 11)

if  computador==1: #computador jogou PEDRA.
    if jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('VOCÊ GANHOU')
    elif jogador==3: 
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')  

elif  computador==2: #computador jogou PAPEL.
    if jogador==1:
        print('COMPUTADOR GANHOU')
    elif jogador==2:
        print('EMPATE')
    elif jogador==3: 
        print('VOCÊ GANHOU')
    else:
        print('JOGADA INVÁLIDA!')  
elif  computador==3: #computador jogou TESOURA.
    if jogador==1:
        print('VOCÊ GANHOU')
    elif jogador==2:
        print('COMPUTADOR GANHOU')
    elif jogador==3: 
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')  