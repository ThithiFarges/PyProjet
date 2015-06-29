#Programme du jeu PyProjet

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *

pygame.init() #On initialise la fenêtre

#VARIABLE ET CONSTANTES
BLANC= (255,255,255)  #Avec le modèle rgb (red, green, blue)

#MISE EN PLACE DE LA FENËTRE

carte=pygame.display.set_mode((1600,700), RESIZABLE) # On ouvre une fenêtre graphique de 440*480 (large*hauteur) + la taille peut s'adapter
pygame.display.set_caption('PyProjet') #On nomme la fenêtre Pyprojet
pygame.mouse.set_visible(1)

carte.fill(BLANC) #On remplit la carte en blanc
pygame.display.update() #On la met à jour
######################################################################################################





#######################################################################################################
continuer = 1
#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
pygame.quit()