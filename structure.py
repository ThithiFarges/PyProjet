### STRUCTURE PRINCIPALE DU PROJET ###

import pygame,sys,time,random #on importe la librairie pygame avec quelques modules
from constantes import *
from pygame.locals import *


pygame.init() #On initialise la fenêtre

carte=pygame.display.set_mode((longueur_fenetre,largeur_fenetre), RESIZABLE) # On ouvre une fenêtre graphique de large*hauteur)
																			 #+ la taille peut s'adapter
pygame.display.set_caption(titre_fenetre) #On nomme la fenêtre Pyprojet
#icone = pygame.image.load(image_icone) #On insère l'icone de la fenêtre
pygame.mouse.set_visible(1)


pygame.time.Clock().tick(30) #Limitation de la vitesse