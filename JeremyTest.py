#Programme du jeu PyProjet

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *

pygame.init() #On initialise la fenêtre

#VARIABLE ET CONSTANTES
BLANC= (255,255,255)  #Avec le modèle rgb (red, green, blue)
GREY=(122,122,82)
BROWN=(102,51,0)
BLEU=(0,0,255)
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
 [1,3,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2 ,2, 2 ,1, 1],
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
#On met les coordonnées du tableau à l'échelle de la fenêtre
def xReel(x):
	x=x*71
	return x

def yReel(y):
	y=y*46
	return y

#Fonction donnant une couleur aux cases en fonction des valeurs du tableau de la carte c'est à dire Str_carte


def Perso(xcoord,ycoord,tour):
	if tour==1:
		xperso=xReel(xcoord)+71/4
		yperso=yReel(ycoord)+46/4
	else:
		xperso=xcoord
		yperso=ycoord
	coul=BLEU
	pygame.draw.rect(carte,coul,(xperso,yperso,71/2,46/2))
	return (xperso,yperso)

def Mur(xcoord,ycoord,genre,tour):
	if genre==1:
		coul=BROWN
	else: 
		coul=GREY
	if tour==1:
		pygame.draw.rect(carte,coul,(xReel(xcoord),yReel(ycoord),71,46))
	else: pygame.draw.rect(carte,coul,(xcoord,ycoord,71/2,46/2))

for x in range(0,20):
	for y in range(0,14):
		if Str_carte[y][x]!=0:
			Mur(x,y,Str_carte[y][x],1)
			if Str_carte[y][x]==3:
				(xperso,yperso)=Perso(x,y,1)
pygame.display.update()

def Verif(futurx,futury):
	if Str_carte[futury/46][futurx/71]!=1:
		return 1

#--------------------------------------------------------------------------------------------------------------------------
def move(xperso,yperso,enx,eny):
	verif=Verif(xperso+enx,yperso+eny)
	if verif==1:
		Mur(xperso,yperso,2,0)
		xperso=xperso+enx
		yperso=yperso+eny
		(xperso,yperso)=Perso(xperso,yperso,0)
		pygame.display.update()
		return (xperso,yperso)
	else:
		pygame.display.update()
		return (xperso,yperso)
	







z=1
while z:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				(xperso,yperso)=move(xperso,yperso,71,0)
			
			if event.key == K_LEFT:
				(xperso,yperso)=move(xperso,yperso,-71,0)

			if event.key == K_UP:
				(xperso,yperso)=move(xperso,yperso,0,-46)

			if event.key == K_DOWN:
				(xperso,yperso)=move(xperso,yperso,0,46)




#--------------------------------------------BOUCLE POUR QUE LA FENETRE REPONDE--------------------------------------------
continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
pygame.quit()