from composante import Composante

class Chassis(Composante):
    def __init__(self, nom, poids, aire_frontale, coefficient_trainee):
        super().__init__(nom, poids)
        self._aire_frontale = aire_frontale
        self._coefficient_trainee = coefficient_trainee
