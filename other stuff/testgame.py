# Importieren der Pygame-Bibliothek
import pygame



# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Fenster öffnen
FENSTERBREITE = 1920
FENSTERHOEHE = 1080

screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

# Titel für Fensterkopf
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()


# Definieren der Variablen
ballpos_x = 100
ballpos_y = 100
ballgr = 100
geschwindigkeit_ball = 5
schwebeeffekt = 1
schwebecount = 1
spielerfigur = pygame.image.load("Tano.png")

print(spielerfigur.get_rect())
''' 
get_rect() / returns a new rectangle covering the entire surface


'''


spielaktiv = False
# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        
        #Spieler hat taste gedrückt
              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                geschwindigkeit_ball *= 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                geschwindigkeit_ball /= 2


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: ballpos_y -= geschwindigkeit_ball
    if keys[pygame.K_s]: ballpos_y += geschwindigkeit_ball
    if keys[pygame.K_a]: ballpos_x -= geschwindigkeit_ball
    if keys[pygame.K_d]: ballpos_x += geschwindigkeit_ball

    # Spiellogik hier integrieren

    # bewegen unseres Kreises
            
    #ball apprallen lassen
        
    if (ballpos_x <= 0):
        ballpos_x = 0
    if (ballpos_x > FENSTERBREITE - ballgr):
        ballpos_x = FENSTERBREITE - ballgr
    if (ballpos_y <= 0):
        ballpos_y = 0
    if (ballpos_y > FENSTERHOEHE - ballgr):
        ballpos_y = FENSTERHOEHE - ballgr
        
    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen

    #pygame.draw.ellipse(screen, ROT, [ballpos_x,ballpos_y,ballgr,ballgr]) #[start_pos X,start_pos Y,breite,höhe]

    screen.blit(spielerfigur,(ballpos_x,ballpos_y))

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(120)

pygame.quit()

