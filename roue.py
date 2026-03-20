from composante import Composante

class Roue(Composante):
    def __init__(self, nom, poids, coefficient_friction, poids_supporte):
        super().__init__(nom, poids)
        self._coefficient_friction = coefficient_friction
        self._poids_supporte = poids_supporte
