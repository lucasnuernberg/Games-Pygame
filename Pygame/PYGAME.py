##Game made by @lucasnuernberg
#Enjoy
import pygame
from random import randint
#dake song
pygame.mixer.init()
pygame.mixer.music.load('drake.mp3')
pygame.mixer.music.play()

blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yeallow = (255, 255, 0)
try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura = 420
altura = 320
tamanho = 10


relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game do Lucas")


def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, yeallow, [XY[0], XY[1], tamanho, tamanho])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, red, [pos_x, pos_y, tamanho, tamanho])


def jogo():
    sair = True
    pos_x = randint(0, (largura - tamanho) / 10) * 10
    pos_y = randint(0, (altura - tamanho) / 10) * 10
    maca_x = randint(0, (largura - tamanho) / 10) * 10
    maca_y = randint(0, (altura - tamanho) / 10) * 10
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    CobraComp = 1
    while sair:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
        fundo.fill(black)
        pos_x += velocidade_x
        pos_y += velocidade_y

        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]

        cobra(CobraXY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint(0, (largura - tamanho) / 10) * 10
            maca_y = randint(0, (altura - tamanho) / 10) * 10
            CobraComp += 1

        maca(maca_x, maca_y)
        pygame.display.update()
        relogio.tick(15)
        if pos_x > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x = largura - tamanho
        if pos_y > altura:
            pos_y = 0
        if pos_y < 0:
            pos_y = altura - tamanho
    ##    if pos_x > largura:
    ##        sair = False
    ##    if pos_x < 0:
    ##        sair = False
    ##    if pos_y > altura:
    ##        sair = False
    ##    if pos_y < 0:
    ##        sair = False
maca(10,10)
jogo()
pygame.quit()


