#Programme du jeu PyProjet

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from pygame.locals import *

pygame.init() #On initialise la fenêtre

#VARIABLE ET CONSTANTES
BLANC= (255,255,255)  #Avec le modèle rgb (red, green, blue)


#MISE EN PLACE DE LA FENËTRE

carte=pygame.display.set_mode((1600,700)) # On ouvre une fenêtre graphique de 440*480 (large*hauteur) en pixel
pygame.display.set_caption('PyProjet') #On nomme la fenêtre Pyprojet
pygame.mouse.set_visible(1)

carte.fill(BLANC) #On remplit la carte en blanc
pygame.display.update() #On la met à jour

#On définit la structure de la carte
Str_carte=[
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0 ,0, 0],
 [0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0 ,0, 0]
]