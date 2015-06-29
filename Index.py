#Programme du jeu PyProjet

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *

pygame.init() #On initialise la fenêtre

#VARIABLE ET CONSTANTES
BLANC= (255,255,255)  #Avec le modèle rgb (red, green, blue)
GREY=(122,122,82)
BROWN=(102,51,0)
#MISE EN PLACE DE LA FENËTRE

carte=pygame.display.set_mode((1500,700), RESIZABLE) # On ouvre une fenêtre graphique de 440*480 (large*hauteur) + la taille peut s'adapter
pygame.display.set_caption('PyProjet') #On nomme la fenêtre Pyprojet
pygame.mouse.set_visible(1)

carte.fill(BLANC) #On remplit la carte en blanc
#pygame.display.update() #On la met à jour
pygame.display.update()
#On définit la structure de la carte
Str_carte=[
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,2,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2 ,2, 2 ,1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#On met les coordonnées du tableau à l'échelle de la fenêtre
def xReel(x):
	x=x*71
	return x

def yReel(y):
	y=y*46
	return y

#Fonction donnant une couleur aux cases en fonction des valeurs du tableau de la carte c'est à dire Str_carte

def Mur(xcoord,ycoord,genre):
	if genre==2:
		coul=GREY
	else: 
		coul=BROWN
	pygame.draw.rect(carte,coul,(xReel(xcoord),yReel(ycoord),71,46))



for x in range(0,20):
	for y in range(0,14):
		if Str_carte[y][x]!=0:
			Mur(x,y,Str_carte[y][x])
			



#--------------------------------------------BOUCLE POUR QUE LA FENETRE REPONDE--------------------------------------------
continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
pygame.quit()