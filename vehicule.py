import numpy as np
import pygame
from specifications import DENSITE_AIR

class Vehicule:
    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):
        self.__nom = nom
        self.__position = np.array(position_dep) 
        self.__vitesse = np.array(0) 
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__poids_total = self.calculer_poids_total
        self.image = pygame.transform.scale(pygame.image.load(image_path), (Specs.image_width, Specs.image_height) )
        
    
    def affichage_vehicule(self, screen):
        screen.blit(self.image, self.__position)
        #pygame.display.update()
    
    def calculer_poids_total(self):
        return sum(roue.get_poids() for roue in self.__roues) + self.__chassis.get_poids() + self.__moteur.get_poids()

    def calculer_traction(self):
        return self.__poids_total * self.__moteur.get_acceleration()

    def calculer_friction(self):
        return self.__roues[0].get_coeff_fric() * self.__vitesse
    
    def calculer_trainee(self):
        return 0.5 * DENSITE_AIR * self.__chassis.get_aire() * self.__chassis.get_coeff_trainee() * self.__vitesse ** 2
 
    def accelerer(self, dt):
        acceleration = (self.calculer_traction - self.calculer_trainee - self.calculer_friction) / self.__poids_total
        self.__vitesse += acceleration * dt
        self.__position += self.__vitesse * dt

    def celebrer(self):
        # TODO : compléter la méthode 
        
        pass # à enlever