Pour intégrer les confettis, j'ai utilisé pygame.rect pour donner les coordonnes d'un confetti et screen.fill pour l'afficher.
## Le constructeur
Le constructeur utilise pygame.Rect et random pour attribuer des valeurs aux attributs d'un confetti.
- vitesse : valeur aléatoire avec random.randint
- forme : object pygame.Rect
- couleur : tuple à 3 valeurs représentant un RGB
- sin_compt : utilisé pour donner le chemin que le confetti suivra
- amplitude : affecte la grandeur de l'onde; initialisé avec random.randint
- frequence : affecte le nombre d'onde en une période; initialisé avec random.randint
- sens : affecte le sens de l'onde; initialisé avec random.randint

# Les fonctions

## assigner_couleur
La fonction utilise *couleurs* et *compteur* pour assigner chaque couleur aux confettis à leur création avec un modulo 4 du compteur. 
- couleurs : tuple qui contient les couleurs à assigner, représenté par des tuples à 3 valeurs. 
- compteur : int initialisé à 0.

## donner_forme
La fonction utilise *x* et *cote* pour construire et retourner un objet pygame.Rect.
- x : la position initiale du confetti sur l'axe des abcisses; initialisé avec random.randint 
- cote : la longueur d'un cote du rectangle; initialisé avec random.randint

## tomber
La fonction utilise les fonctions *sin* et *radians* importé de math et les attributs *sin_compt*, *frequence*, *amplitude*, *sens* et *vitesse* pour animer le confetti durant sa chute. Elle appelle la fonction move() du rectangle pour retourner un nouveau rectangle s'ayant déplacé du décalage donné en paramètre.
- décalage en x : donné par un calcul sinusoïdale
- décalage en y : donné par la vitesse de l'objet

## afficher_confetti
La fonction prend en paramètre un pygame.display qui appelle la méthode fill() pour afficher le confetti. Celui-ci prend en paramètre la couleur et la forme du confetti.

# Intégration dans main
Avant la boucle principale du jeu, j'ai initialisé une liste que j'ai rempli avec 100 objets Confetti. Puis, dans la condition qui s'exécute seulement si on a un gagnant, j'ai mis une boucle for qui appelle les fonctions tomber() et afficher_confetti(). De plus, si un confetti dépasse le bas de l'écran, on l'enlève de la liste.
