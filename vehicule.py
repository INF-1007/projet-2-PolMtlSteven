import numpy as np
import pygame
from specifications import DENSITE_AIR

class Vehicule:
    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):
        self.__nom = nom
        self.__position = np.full(int, position_dep) # Tester ceci
        self.__vitesse = np.zeros(int) # Tester bon format
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__poids_total = self.__roues.get_poids() + self.__chassis.get_poids() + self.__moteur.get_poids()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (Specs.image_width, Specs.image_height) )
        
    
    def affichage_vehicule(self, screen):
        # TODO : compléter la méthode 

        pass # à enlever
    
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