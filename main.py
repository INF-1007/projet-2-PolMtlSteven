import pygame
from moto import Moto
from auto import Auto
from camion import Camion
from confettis import Confetti
from config import WIDTH, HEIGHT, START_LINE_X, FINISH_LINE_X, START_MOTO_Y, START_AUTO_Y, START_CAMION_Y 


def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulation de course")

    background = pygame.image.load("images/background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    moto1 = Moto("Le Rangeur Grognant", (START_LINE_X, START_MOTO_Y)) 
    auto1 = Auto("Le Sordide Assomeur", (START_LINE_X, START_AUTO_Y))
    cam1 = Camion("Le Porridgeur à Porridger", (START_LINE_X, START_CAMION_Y))

    liste_vehic = [moto1, auto1, cam1]


    running = True
    course_commencee = False
    gagnant = None

    while running:

        screen.blit(background, (0, 0))

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    course_commencee = True

        # TODO : Gérer le début de la course en appelant la méthode `accelerer` des véhicules
        # Si le véhicule franchit la ligne et qu’on n’a pas encore de gagnant, on le note


        for vehic in liste_vehic:
            vehic.affichage_vehicule(screen)
        

        if not course_commencee and gagnant is None:
            txt = font.render("Appuyez sur ESPACE pour démarrer",
                              True, (0, 0, 0))
            screen.blit(txt, (350, 35))

        # TODO: Si on a un gagnant, afficher le message qui indique le véhicule gagnant avec la méthode `celebrer` 
        

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()