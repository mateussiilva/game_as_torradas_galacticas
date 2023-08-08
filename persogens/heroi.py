
from pygame.sprite import Sprite
from pygame.image import load
import pygame

class DunoFausto(Sprite):
    
    def __init__(self,size,grupo_torradas,qtd_poder:int=5) -> None:
        super().__init__()

        self.image = load('images/dunofausto_small.png')
        self.rect = self.image.get_rect()
        # self.torradas = torradas
        self.grupo_torradas = grupo_torradas
        self.velocidade = 1.5
        self.quantidade_poder = qtd_poder
        self.size = size

    def tacar_torrada(self):
        toast = Torradas(*self.rect.center)
        if len(self.grupo_torradas) <= self.quantidade_poder:
            self.grupo_torradas.add(toast)
        


    def update(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]: # ESQUERDA
            if self.rect.x > 0:
                self.rect.x -= self.velocidade

        if keys[pygame.K_RIGHT]: # DIREITA
            if self.rect.x  < self.size[0] - 100:
                self.rect.x += self.velocidade
        
        if keys[pygame.K_DOWN]:# BAIXO
            if self.rect.y < self.size[1] - 100:
                self.rect.y += self.velocidade

        if keys[pygame.K_UP]: # CIMA
            if self.rect.y > 0:
                self.rect.y -= self.velocidade


class Torradas(Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = load('images/toast_small.png')
        self.rect = self.image.get_rect(
            center=(x,y)
        )
 
    def update(self):
        self.rect.x += 1

