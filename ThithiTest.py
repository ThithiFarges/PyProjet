#Programme du jeu PyProjet

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *

pygame.init() #On initialise la fenêtre
pygame.key.set_repeat(10, 200) #permet de continuer la déplacement en restant appuyer sur la touche

#VARIABLE ET CONSTANTES
BLANC= (255,255,255)  #Avec le modèle rgb (red, green, blue)
GREY=(122,122,82)
BROWN=(102,51,0)
BLEU=(0,0,255)
NOIR=(0,0,0)
BLEUGRIS=(85,128,170)
YELLOW=(255, 255, 71)
#MISE EN PLACE DE LA FENËTRE

carte=pygame.display.set_mode((1500,700), RESIZABLE) # On ouvre une fenêtre graphique de 440*480 (large*hauteur) + la taille peut s'adapter
pygame.display.set_caption('PyProjet') #On nomme la fenêtre Pyprojet
pygame.mouse.set_visible(1) #on rend visible la souris sur l'écran

carte.fill(BLANC) #On remplit la carte en blanc
#pygame.display.update() #On la met à jour
pygame.display.update()

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
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,4,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,1,1,1,1,1,2,1,1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
 [1,2,2,2,2,2,2,2,2,2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.display.update()
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


def egaux():
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

#################################################################################
# 																				#
# 																				#
# 																				#
# 		       				DEBUT DE LA BOUCLE PRINCIPALE						#
# 																				#
# 																				#
# 																				#
#################################################################################


for x in range(0,20):
	for y in range(0,14):
		if Str_carte[y][x]!=0:
			Case(x,y,Str_carte[y][x],1)
			if Str_carte[y][x]==3:
				(xperso,yperso)=Perso(x,y,1,1)
				(xperso2,yperso2)=Perso(x,y,1,2)
pygame.display.update()

tirer(0,0,1)

continuer=1

while continuer:
	for event in pygame.event.get():

		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				(xperso,yperso)=move(xperso,yperso,71,0,1)
			
			if event.key == K_LEFT:
				(xperso,yperso)=move(xperso,yperso,-71,0,1)

			if event.key == K_UP:
				(xperso,yperso)=move(xperso,yperso,0,-46,1)

			if event.key == K_DOWN:
				(xperso,yperso)=move(xperso,yperso,0,46,1)
			
			if event.key== K_w:
				(xperso2,yperso2)=move(xperso2,yperso2,0,-46,2)

			if event.key== K_a:
				(xperso2,yperso2)=move(xperso2,yperso2,-71,0,2)

			if event.key== K_s:
				(xperso2,yperso2)=move(xperso2,yperso2,0,46,2)

			if event.key== K_d:
				(xperso2,yperso2)=move(xperso2,yperso2,71,0,2)

		if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0

pygame.quit()