"""Projet NSI
Jeu de mémoire SIMON """


import pygame,sys,time
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

pygame.init()
pygame.mixer.init()
sonBleu=pygame.mixer.Sound("bleu.wav")
sonRouge=pygame.mixer.Sound("rouge.wav")
sonVert=pygame.mixer.Sound("vert.wav")
sonJaune=pygame.mixer.Sound("jaune.wav")
#sonBleu.play()
#time.sleep(1)
#sonRouge.play()
#sonJaune.play()
sonVert.play()
fenetre=pygame.display.set_mode((640,580))
while True:
    pygame.draw.rect(fenetre,(255,0,0),(0,0,320,240))
    pygame.draw.rect(fenetre,(0,255,0),(0,240,320,240))
    pygame.draw.rect(fenetre,(0,0,255),(320,0,320,240))
    pygame.draw.rect(fenetre,(255,255,0),(320,240,320,240))
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

