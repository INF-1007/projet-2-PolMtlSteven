import random
import pygame
from config import  WIDTH
from math import sin, radians

class Confetti: 
    compteur = -1
    
    couleurs = (
        (0, 0, 255), # bleu
        (0, 255, 0), # vert
        (255, 0, 0), # rouge
        (255, 255, 255) # blanc
    )

    def __init__(self):
        self.__vitesse = random.uniform(3, 20)
        self.__forme = self.donner_forme()
        self.__couleur = self.assigner_couleur()
        self.__sin_compt = 0
        self.__amplitude = random.randint(5, 10)
        self.__frequence = random.randint(5, 20)
        self.__sens = 1 if random.random() < 0.5 else -1

    def assigner_couleur(self):
        type(self).compteur += 1
        return type(self).couleurs[type(self).compteur % 4]
    
    def donner_forme(self):
        x = random.randint(0, WIDTH)
        cote = random.randint(5, 20)
        return pygame.Rect(x, 0, cote, cote)

    def tomber(self):
        self.__forme = self.__forme.move(self.__amplitude * self.__sens * sin(radians(self.__sin_compt)), self.__vitesse)
        self.__sin_compt += self.__frequence

    def afficher_confetti(self, screen):
        screen.fill(self.__couleur, self.__forme)

    def get_forme(self):
        return self.__forme

    