from vehicule import Vehicule
from roue import Roue
from moteur import Moteur
from chassis import Chassis
from specifications import CamionSpecs

class Camion(Vehicule): 
    
    cam_roue = Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support)
    cam_roues = (cam_roue, cam_roue, cam_roue, cam_roue, cam_roue, cam_roue)
    cam_moteur = Moteur(CamionSpecs.moteur_nom, CamionSpecs.moteur_poids, CamionSpecs.moteur_acceleration)
    cam_chassis = Chassis(CamionSpecs.chassis_nom, CamionSpecs.chassis_poids, CamionSpecs.chassis_aire, CamionSpecs.chassis_trainee)
    image_path = "images/camion.png"

    def __init__(self, nom, position_dep):
        super().__init__(nom, position_dep, type(self).cam_roues, type(self).cam_moteur, 
                         type(self).cam_chassis, CamionSpecs, type(self).image_path)