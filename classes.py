#!/usr/bin/python3
# -*- coding: Utf-8 -*
#################################################################################
# 																				#
# 																				#
# 																				#
# 		       				DECLARATION DES CLASSES DU JEU						#
# 																				#
# 																				#
# 																				#
#################################################################################

import pygame
from pygame.locals import * 
from constantes import *

carte=pygame.display.set_mode((longueur_fenetre,largeur_fenetre), RESIZABLE)

#On met les coordonnées du tableau à l'échelle de la fenêtre
def xReel(x):
	x=x*71
	return x

def yReel(y):
	y=y*46
	return y

#Fonction donnant une couleur aux cases en fonction des valeurs du tableau de la carte c'est à dire Str_carte

def Perso(xcoord,ycoord,tour,nb):
	if tour==1:
		xperso=xReel(xcoord)+71/4
		yperso=yReel(ycoord)+46/4
		
	else:
		xperso=xcoord
		yperso=ycoord
	
	if nb==1:
		coul=BLEU
		pygame.draw.rect(carte,coul,(xperso,yperso,71/2,46/2))
	if nb==2:
		coul=NOIR
		pygame.draw.rect(carte,coul,(xperso,yperso,71/2,46/2))
	return (xperso,yperso)

def Case(xcoord,ycoord,genre,tour):
	if genre==1:
		coul=BROWN
	elif genre==4:
		coul=BLEUGRIS
	else:
		coul=GREY
	if tour==1:
		pygame.draw.rect(carte,coul,(xReel(xcoord),yReel(ycoord),71,46))
	else: 
		if coul==BLEU or coul==NOIR:
			pygame.draw.rect(carte,coul,(xcoord,ycoord,71/2,46/2))
		else:
			pygame.draw.rect(carte,coul,(xcoord-71/4,ycoord-46/4,71,46))

#On définit la structure de la carte

Str_carte=[
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,3,2,2,2,4,2,2,2,2, 2, 2, 2, 2, 2, 2, 2 ,2, 2 ,1, 1],
 [1,2,1,1,1,1,1,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,4,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
 [1,2,1,1,1,1,1,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,2,2,2,2,1,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,2,2,1,2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
 [1,1,1,2,1,1,2,1,1,2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1],
 [1,1,1,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
def Echange(coord1, coord2, coord3, coord4):

	a=Str_carte[coord1/46][coord2/71]
	b=Str_carte[coord3/46][coord4/71]
	Str_carte[coord3/46][coord4/71]=a
	Str_carte[coord1/46][coord2/71]=b
	pygame.display.update()

def Verif(futurx,futury,mur): #on vérifie la position du joueur
	if Str_carte[futury/46][futurx/71]==2 or Str_carte[futury/46][futurx/71]==3:
		if mur==1:
			if xperso==futurx and yperso==futury or xperso2==futurx and yperso2==futury:
				return 0
			else:
				return 1
		else:
			return 1
	if Str_carte[futury/46][futurx/71]==4:
		return 2

global xperso,yperso,xperso2,yperso2
"""xperso=1
yperso=2
xperso2=3
yperso2=4"""

def egaux():
	#global xperso,yperso,xperso2,yperso2
	if xperso==xperso2 and yperso==yperso2:
		coord=1
	else:
		coord=0
	return coord

def moveperso(xperso,yperso,de_x,de_y,nb):
	coord=egaux()
	if coord==0:
		Case(xperso,yperso,2,0)
	if coord==1:
		Perso(xperso,yperso,2,3-nb)
	xperso=xperso+de_x
	yperso=yperso+de_y
	(xperso,yperso)=Perso(xperso,yperso,0,nb)
	return (xperso,yperso)

def move(xperso,yperso,de_x,de_y,nb):
	verif=Verif(xperso+de_x,yperso+de_y,0)
	if verif==1:
		(xperso,yperso)=moveperso(xperso,yperso,de_x,de_y,nb)
		pygame.display.update()
		return (xperso,yperso)
	if verif==2:
		verifmur=Verif(xperso+2*de_x,yperso+2*de_y,1)
		if verifmur==1:
			Case(xperso+de_x,yperso+de_y,2,0)
			Case(xperso+2*de_x,yperso+2*de_y,4,0)
			(xperso,yperso)=moveperso(xperso,yperso,de_x,de_y,nb)
			Echange(yperso, xperso, yperso+de_y, xperso+de_x)
			pygame.display.update()
			return (xperso,yperso)
		else:
			pygame.display.update()
			return (xperso,yperso)
	else:
		pygame.display.update()
		return (xperso,yperso)

def tirer(xperso,yperso,direction):
	x_debut=0
	x_fin=3
	while x_fin <18:
		#pygame.time.wait(500)
		#pygame.time.delay(2000)
		for initial in range(x_debut,x_fin):
			x_projectile=xReel(xperso)+xReel(initial)
			y_projectile=yReel(yperso)+20
			pygame.draw.rect(carte, YELLOW, (x_projectile,y_projectile,71/4,46/4))
		x_debut+=1
		x_fin+=1
	return(xperso,yperso)