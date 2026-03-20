import numpy as np
import pygame
from specifications import DENSITE_AIR

class Vehicule:
    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):
        self.__nom = nom
        self.__position = np.array(position_dep) 
        self.__vitesse = np.array([0, 0]) 
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__poids_total = sum(roue.get_poids() for roue in self.__roues) + self.__chassis.get_poids() + self.__moteur.get_poids()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (Specs.image_width, Specs.image_height) )
        
    
    def affichage_vehicule(self, screen):
        screen.blit(self.image, self.get_position())
        #pygame.display.update()
    
    def calculer_poids_total(self):
        # TODO : compléter la méthode
        
        pass # à enlever

    def calculer_traction(self):
        # TODO : compléter la méthode 
        
        pass # à enlever

    def calculer_friction(self):
        # TODO : compléter la méthode 
        
        pass # à enlever

    def calculer_trainee(self):
        # TODO : compléter la méthode 
        
        pass # à enlever

    def accelerer(self, dt):
        # TODO : compléter la méthode 
        
        pass # à enlever

    def celebrer(self):
        # TODO : compléter la méthode 
        
        pass # à enlever

    def get_position(self):
        return self.__position