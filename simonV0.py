"""Projet NSI
Jeu de mémoire SIMON
Codé par Y. SALAUN le 26/04/2020"""

import pygame,sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

pygame.init()

jaune=(255,255,0)
rouge=(255,0,0)
vert=(0,255,0)
bleu=(0,0,255)
blanc=(255,255,255)
noir=(0,0,0)

fenetre=pygame.display.set_mode((640,580))


while True:
    pygame.draw.rect(fenetre,rouge,(0,0,320,240))
    pygame.draw.rect(fenetre,vert,(0,240,320,240))
    pygame.draw.rect(fenetre,bleu,(320,0,320,240))
    pygame.draw.rect(fenetre,jaune,(320,240,320,240))
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()