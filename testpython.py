#Programme du jeu PyProjet

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *


pygame.init()
longueur_fenetre=1500
largeur_fenetre=700
titre_fenetre= 'PyGame'

BLANC= (255,255,255)
GREY=(122,122,82)
BROWN=(102,51,0)
BLEU=(0,0,255)
NOIR=(0,0,0)

carte=pygame.display.set_mode((longueur_fenetre,largeur_fenetre), RESIZABLE)
pygame.display.set_caption(titre_fenetre)
pygame.mouse.set_visible(1)

pygame.key.set_repeat(10, 200)
pygame.time.Clock().tick(30)

carte.fill(BLANC)
pygame.display.update()
Str_carte=[
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,2,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2 ,2, 2 ,1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

imgjoueur1= pygame.image.load("Nibbler.jpg").convert()
#imgjoueur2=pygame.image.load('Nibbler.jpg').convert()
#imgmur=pygame.draw.rect(carte,BROWN,71,46)

def xReel(x):
	x=x*(longueur_fenetre/21)
	return x
def yReel(y):
	y=y*(largeur_fenetre/15)
	return y
def Personnage(xpersonnage,ypersonnage,numero):
	if numero==1:
		carte.blit(imgjoueur1,(xpersonnage,ypersonnage))
	else:
		carte.blit(imgjoueur1,(xpersonnage,ypersonnage))
	return (xpersonnage,ypersonnage)

def Case():
	for x in range(0,20):
		for y in range(0,14):
			if Str_carte[y][x]==1:
				pygame.draw.rect(carte,BROWN,(xReel(x),yReel(y),71,46))
			elif Str_carte[y][x]==2:
				pygame.draw.rect(carte,GREY,(xReel(x),yReel(y),71,46))
			#else:
				#pygame.draw.rect(carte,NOIR,(xReel(x),yReel(y),71,46))


def bouger(xperso,yperso):
	continuer = 1	
	while continuer:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					xperso=xperso+71
					yperso=yperso
					(xpersonnage,ypersonnage)=Personnage(xperso,yperso,1)
					print xperso
					return (xperso,yperso)
				if event.key == K_LEFT:
					xperso=xperso-71
					yperso=yperso
					(xpersonnage,ypersonnage)=Personnage(xperso,yperso,1)
					return (xperso,yperso)
				if event.key == K_DOWN:
					xperso=xperso
					yperso=yperso+46
					(xpersonnage,ypersonnage)=Personnage(xperso,yperso,1)
					return (xperso,yperso)
				if event.key == K_UP:
					xperso=xperso
					yperso=yperso-46
					(xpersonnage,ypersonnage)=Personnage(xperso,yperso,1)
					return (xperso,yperso)
			if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
					continuer = 0

			pygame.display.update()
	pygame.quit()




Case()
(xpersonnage,ypersonnage)=Personnage(xReel(2),yReel(1),1)
pygame.display.update()
bouger(xpersonnage,ypersonnage)
pygame.display.update()
	

