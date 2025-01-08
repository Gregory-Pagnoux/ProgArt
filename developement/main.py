import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ----------------------------------- Fonction pour dessiner une ligne -----------------------------------
def dessiner_ligne(screen, start_pos, end_pos, couleur, epaisseur=1):
    pygame.draw.line(screen, couleur, start_pos, end_pos, epaisseur)

# EXEMPLE : dessiner_ligne(screen, (50, 50), (750, 550), "red", 5)

# ----------------------------------- Fonction pour dessiner un cercle -----------------------------------
def dessiner_cercle(screen, position, rayon, couleur):
    pygame.draw.circle(screen, position, rayon, couleur)

# EXEMPLE : dessiner_cercle(screen, (400, 300), 50, "blue")

# ----------------------------------- Fonction pour dessiner un carré -----------------------------------
def dessiner_carre(screen, position, taille, couleur):
    pygame.draw.rect(screen, couleur, pygame.Rect(position[0], position[1], taille, taille))

# EXEMPLE : dessiner_carre(screen, (500, 100), 100, "pink")

# ----------------------------------- Fonction pour dessiner un rectangle -----------------------------------
def dessiner_rectangle(screen, position, largeur, hauteur, couleur):
    pygame.draw.rect(screen, couleur, pygame.Rect(position[0], position[1], largeur, hauteur))

# EXEMPLE : dessiner_rectangle(screen, (100, 100), 200, 100, "purple")

# ----------------------------------- Fonction pour dessiner un triangle -----------------------------------
def dessiner_triangle(screen, position, taille, couleur):
    # Les trois sommets du triangle équilatéral
    x, y = position
    points = [
        (x, y - taille),
        (x - taille * math.cos(math.radians(30)), y + taille * math.sin(math.radians(30))),
        (x + taille * math.cos(math.radians(30)), y + taille * math.sin(math.radians(30))),
    ]
    pygame.draw.polygon(screen, couleur, points)

# EXEMPLE : dessiner_triangle(screen, (400, 300), 100, "blue")

# ----------------------------------- Fonction pour dessiner un losange -----------------------------------
def dessiner_losange(screen, position, largeur, hauteur, couleur):
    x, y = position
    points = [
        (x, y - hauteur),
        (x - largeur, y),
        (x, y + hauteur),
        (x + largeur, y)
    ]
    pygame.draw.polygon(screen, couleur, points)

# EXEMPLE : dessiner_losange(screen, (600, 400), 100, 150, brown)

# ----------------------------------- Fonction pour dessiner un hexagone -----------------------------------
def dessiner_hexagone(screen, position, rayon, couleur):
    # Calcul des points de l'hexagone
    points = []
    for i in range(6):
        angle = math.radians(i * 60)
        x = position[0] + rayon * math.cos(angle)
        y = position[1] + rayon * math.sin(angle)
        points.append((x, y))
    
    pygame.draw.polygon(screen, couleur, points)

# EXEMPLE : dessiner_hexagone(screen, (300, 500), 60, "orange")

# ----------------------------------- Fonction pour dessiner une étoile -----------------------------------
def dessiner_etoile(screen, position, rayon, couleur, points=5):
    # Calcul des sommets de l'étoile
    angle = math.pi / points
    points_list = []
    for i in range(2 * points):
        angle_offset = angle * i
        r = rayon if i % 2 == 0 else rayon / 2
        x = position[0] + r * math.cos(angle_offset)
        y = position[1] - r * math.sin(angle_offset)
        points_list.append((x, y))
    
    pygame.draw.polygon(screen, couleur, points_list)

# EXEMPLE : dessiner_etoile(screen, (200, 400), 100, "black")

# ---------------------------------------------------------------------------------------
# ----------------------------------- A VOUS DE JOUER -----------------------------------
# ---------------------------------------------------------------------------------------

# Initialisation de pygame
pygame.init()

# Dimensions de l'écran
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ProgArt")

# Couleur de fond de l'écran
screen.fill("white")

#TODO

# Mettre à jour l'affichage
pygame.display.flip()

# Attente pour fermer la fenêtre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
