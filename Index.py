#!/usr/bin/python3
# -*- coding: Utf-8 -*
#################################################################################
# 																				#
# 																				#
# 																				#
# 		       				        JEU PYPROJET         						#
# 																				#
# 																				#
# 																				#
# 																				#
# Fichiers : index.py, classes.py, constantes.py								#
#################################################################################

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *
from constantes import *
from classes import *

#On initialise la fenêtre
pygame.init() 

#permet de continuer la déplacement en restant appuyer sur la touche
pygame.key.set_repeat(10, 200)

#MISE EN PLACE DE LA FENËTRE

# On ouvre une fenêtre graphique de (large*hauteur) et la taille peut s'adapter
#carte=pygame.display.set_mode((longueur_fenetre,largeur_fenetre), RESIZABLE) 

#On nomme la fenêtre Pyprojet
pygame.display.set_caption(titre_fenetre) 

#On rend visible la souris sur l'écran
pygame.mouse.set_visible(1) 
"""
carte.fill(BLANC) #On remplit la carte en blanc
pygame.display.update() #On la met à jour
"""
#################################################################################
# 																				#
# 																				#
# 																				#
# 		       				DEBUT DE LA BOUCLE PRINCIPALE						#
# 																				#
# 																				#
# 																				#
#################################################################################

continuer=1

while continuer:
	pygame.time.Clock().tick(30)
	for x in range(0,20):
		for y in range(0,14):
			if Str_carte[y][x]!=0:
				Case(x,y,Str_carte[y][x],1)
				if Str_carte[y][x]==3:
					(xperso,yperso)=Perso(x,y,1,1)
					(xperso2,yperso2)=Perso(x,y,1,2)
	pygame.display.update()  #Permet d'afficher directement la map sans temps de latence
	tirer(0,0,1)


	continuer_jeu=1
	continuer_accueil=1

	for event in pygame.event.get():
		#permet de fermer le jeux
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer = 0
			continuer_jeu=0
			continuer_accueil=0

		elif event.type == KEYDOWN:
			if event.key == K_RIGHT:
				(xperso,yperso)=move(xperso,yperso,71,0,1)
			
			elif event.key == K_LEFT:
				(xperso,yperso)=move(xperso,yperso,-71,0,1)

			elif event.key == K_UP:
				(xperso,yperso)=move(xperso,yperso,0,-46,1)

			elif event.key == K_DOWN:
				(xperso,yperso)=move(xperso,yperso,0,46,1)
			
			elif event.key== K_w:
				(xperso2,yperso2)=move(xperso2,yperso2,0,-46,2)

			elif event.key== K_a:
				(xperso2,yperso2)=move(xperso2,yperso2,-71,0,2)

			elif event.key== K_s:
				(xperso2,yperso2)=move(xperso2,yperso2,0,46,2)

			elif event.key== K_d:
				(xperso2,yperso2)=move(xperso2,yperso2,71,0,2)

pygame.quit()