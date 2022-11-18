import inspect
import random
import time

gameabfrage= True
spielrunden= 0

vers = '0.1.0'

class Player():
    #Player-data gespeiert als Objekt  ,magic,hp,doge,defence,ressistence
    def __init__(self,name,exp,lvl,str,dex,int,vit,agil,end,wp,klasse):
        self.name = name
        self.exp = exp
        self.lvl = lvl
        self.str = str #strength
        self.dexterity = dex # dexterity
        self.int = int #intelligence
        self.vit = vit #vitality
        self.agil = agil #agility
        self.end = end #endurence
        self.wp = wp #willpower
        self.atk = str + lvl
        self.pre = dex + lvl #precision
        self.mag = int + lvl #magic
        self.hp = vit + lvl
        self.doge = agil + lvl
        self.defence = end + lvl
        self.res = wp + lvl #resistence
        self.klasse = klasse
class Monster():
    #Monster-data gespeiert als Objekt
    def __init__(self,name,exp,lvl,atk,hp):
        self.name = name
        self.exp = exp
        self.lvl = lvl
        self.atk = atk
        self.hp = hp

def kampf(a,b):
    
    if a.atk > b.atk:
        return True

    else:
        time.sleep(1)
        print('Kampf verloren')
        return False

slime = Monster('Slime',1,1,1,1)
minotaurus = Monster('Minotaurus',5,2,10,1)
monsterlist = [slime,minotaurus]

player = Player(input('Wie heist du?'),0,1,1,1,1,1,1,1,1,0)
time.sleep(1)
print('Hallo',player.name,'\nWilkommen in Antallia V:',vers)


while gameabfrage == True:
    time.sleep(1)
    aktion=int(input('Was möchtest du tun? \n1.Kämpfen\n2.Ruhen\n'))
    #Kämpfen
    if aktion == 1:
        monster = random.choice(monsterlist)
        time.sleep(1)
        print('Du kämpfst gegen: ',monster.name)
        if  kampf(player,monster) == True:
            player.exp=player.exp+1
            if player.exp%10 == 0:
                player.lvl=player.lvl+1
                player.atk=player.atk+1
                time.sleep(1)
                print('LEVEL UP')
        else:
            player.hp=player.hp-1
    #Ruhen
    if aktion == 2:
        player.hp =player.hp +5
        if player.exp%10 == 0:
            player.lvl=player.lvl+1
            player.atk=player.atk+1
            player.exp=player.exp+1
    #Tod
    if player.hp == 0:
        if int(input('Weiterspielen? 1. JA 0. NEIN'))==1:
            spielrunden = spielrunden+1
        else:
            time.sleep(1)
            print('Danke fürs Spielen')
            gameabfrage=False
    #Status
    if aktion == 3:
        print(inspect.getmembers(player))

