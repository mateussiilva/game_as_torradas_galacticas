
import pygame
from time import sleep
from pygame import display, event
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import  Group,GroupSingle, groupcollide
from pygame.locals import QUIT,KEYUP,K_SPACE,KEYDOWN,K_k
from pygame.time import Clock
from persogens.heroi import DunoFausto,Torradas
from persogens.inimigo import Inimigo

 
# INICIO O PYAGAME
pygame.init()

# PROPRIEDADES DA JANELA
size= 800,600
superfice = display.set_mode(display=0,size=size)
display.set_caption("Testes de Pyagame")
fundo = scale(load("images/space.jpg"), size=size)

grupo_inimigos = Group()
grupo_torradas = Group()
grupo_herois = GroupSingle()

heroi = DunoFausto(
    grupo_torradas=grupo_torradas,
    size=size)

grupo_herois.add(heroi)
clock = Clock()
mortes = 0
round = 0
contatador_torradas = 0
while True:
    # ESPAÇO DO DISPALY
    superfice.blit(fundo,(0,0))
    clock.tick(240) # FPS
    if round % 240 == 0:
        grupo_inimigos.add(Inimigo())

    # ESPAÇO PARA LER OS EVENTOS
    for evento in event.get():
        if evento.type == QUIT or mortes == 1: #EVENTO PARA FECHAR O JOGO
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                contatador_torradas += 1
                heroi.tacar_torrada()
                print(f"Taquei {contatador_torradas}")

        if evento.type == KEYDOWN:
            if evento.key == K_k:
                print("Vou soltar a ULTIMATE DO PERSONAGEM")
                heroi.ultimate()
    if groupcollide(grupo_torradas,grupo_inimigos,True,True): # MATEI O INIMGO
        mortes += 1
        print("Torrada bateu no inimigo")
    
    if groupcollide(grupo_herois,grupo_inimigos,True,True):
        print("GAME OVER")
        pygame.quit()
    
    # DESENHA OS GRUPOS NA TELA  
    grupo_herois.draw(superfice)
    # grupo_inimigos.draw(superfice)
    # grupo_torradas.draw(superfice)
    
    
    # ATUALIZA OS GRUPOS NA TELA
    grupo_herois.update()
    # grupo_inimigos.update()
    # grupo_torradas.update()

    # ATUALIZA A TELA EM SI
    display.update()
    round += 1

