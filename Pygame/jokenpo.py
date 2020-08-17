#Jokenpo Game
from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
while True:
    computador = randint(0, 2)
    print('PEDRA[0]')
    print('PAPEL[1]')
    print('tesoura[2]')
    print('sair[3]')
    eu = int(input('ESCOLHA PEDRA PAPEL TESOURA: '))#ESCOLHA DO JOGADOR
    if eu == 3:
        break
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('')
    if computador == 0:
        if eu == 0:
            print('empate')
        elif eu == 1:
            print('Você ganhou!')
        elif eu == 2:
            print('pc ganhou')
        else:
            print('jogada inválida')
    elif computador == 1:
        if eu == 0:
            print('computador ganhou')
        elif eu == 1:
            print('empate')
        elif eu == 2:
            print('Você ganhou!')
        else:
            print('jogada inválida')
    elif computador == 2:
        if eu == 0:
            print('PC ganhou')
        elif eu == 1:
            print('Você ganhou!')
        elif eu == 2:
            print('empate')
        else:
            print('jogada inválida')
    


    print('O computador escolheu {}'.format(itens[computador]))
    print('Você jogou {}'.format(itens[eu]))
    print('-'*30)