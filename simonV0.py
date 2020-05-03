"""Projet NSI - Jeu de mémoire SIMON
Codé par Y. SALAUN le 26/04/2020"""

import pygame,sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

pygame.init()

jaune=(255,255,0)
jaune2=(255,255,107)
rouge=(255,0,0)
rouge2=(233,56,63)
vert=(0,255,0)
vert2=(84,249,141)
bleu=(0,0,255)
bleu2=(0,127,255)
blanc=(255,255,255)
noir=(0,0,0)

#Définition des rectangles de couleur :

rect_rouge=pygame.Rect(0,0,320,240)#
rect_bleu=pygame.Rect(320,0,320,240)#
rect_vert=pygame.Rect(0,240,320,240)#
rect_jaune=pygame.Rect(320,240,320,240)#

liste_rect=[rect_rouge,rect_bleu,rect_vert,rect_jaune]#

#les sons

pygame.mixer.init()
sonBleu=pygame.mixer.Sound("bleu.wav")
sonRouge=pygame.mixer.Sound("rouge.wav")
sonVert=pygame.mixer.Sound("vert.wav")
sonJaune=pygame.mixer.Sound("jaune.wav")

fenetre=pygame.display.set_mode((640,580))

def jouer(r):
    if r == rect_rouge:
        pygame.draw.rect(fenetre,rouge2,r)
        sonRouge.play()
    elif r == rect_bleu:
        pygame.draw.rect(fenetre,bleu2,r)
        sonBleu.play()
    elif r == rect_vert:
        pygame.draw.rect(fenetre,vert2,r)
        sonVert.play()
    else:
        pygame.draw.rect(fenetre,jaune2,r)
        sonJaune.play()

def afficher():
    pygame.draw.rect(fenetre,rouge,(0,0,320,240))
    pygame.draw.rect(fenetre,vert,(0,240,320,240))
    pygame.draw.rect(fenetre,bleu,(320,0,320,240))
    pygame.draw.rect(fenetre,jaune,(320,240,320,240))

afficher()

while True:
    
    for event in GAME_EVENTS.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#
            pos=pygame.mouse.get_pos()#
            for r in liste_rect:#
                if r.collidepoint(pos):#
                    jouer(r)#
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            afficher()
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()