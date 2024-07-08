import json
import pygame
pygame.init()

#daten Laden
entity=json.loads(open("entity.json","r").read())
player=entity
monster = entity
playerpng = pygame.image.load("Tano.png")
 

# Fenster öffnen
def window(a,b):
    return pygame.display.set_mode((a, b))

screen = window(1920,1080)


#positionen der Gegner
def monster(name,hp,exp):
    name = entity
    name["name"] = name
    name["exp"] = exp
    name["kampfwerte"]["hp"] = hp

slime = monster("slime",3,5)


#gameloop
game=True
while game==True:
# eventabfrage
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False
   
    if pygame.key.get_pressed()[pygame.K_w]: player["position"]["y"] += 1
    if pygame.key.get_pressed()[pygame.K_s]: player["position"]["y"] -= 1
    if pygame.key.get_pressed()[pygame.K_a]: player["position"]["x"] += 1
    if pygame.key.get_pressed()[pygame.K_d]: player["position"]["x"] -= 1
    
#werteberechnung
    player["kampfwerte"]["atk"] = player["basiswerte"]["str"]+5
    
#fenster Löschen
    screen.fill((0,0,0))
#fenster zeichen
    #gegner


    #player zeichnen
    screen.blit(playerpng,(((screen.get_rect().width)/2)-(playerpng.get_rect().width)/2,(screen.get_rect().height)/2-(playerpng.get_rect().height)/2))

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    pygame.time.Clock().tick(120)
#open("player.json","w").write(json.dumps(player))
pygame.quit()

