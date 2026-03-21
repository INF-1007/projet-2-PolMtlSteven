# moto.py
from vehicule import Vehicule
from specifications import MotoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Moto(Vehicule):
    moto_roue = Roue(MotoSpecs.roue_nom, MotoSpecs.roue_poids, MotoSpecs.roue_friction, MotoSpecs.roue_support)
    moto_roues = (moto_roue, moto_roue)
    moto_moteur = Moteur(MotoSpecs.moteur_nom, MotoSpecs.moteur_poids, MotoSpecs.moteur_acceleration)
    moto_chassis = Chassis(MotoSpecs.chassis_nom, MotoSpecs.chassis_poids, MotoSpecs.chassis_aire, MotoSpecs.chassis_trainee)
    image_path = "images/moto.png"

    def __init__(self, nom, position_dep):
        super().__init__(nom, position_dep, type(self).moto_roues, type(self).moto_moteur, 
                         type(self).moto_chassis, MotoSpecs, type(self).image_path)