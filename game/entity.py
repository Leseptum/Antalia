import json

class Player:

    def createStats(self,name,strength,dexterity,intelligence,constitution,charisma,willpower,temphealth,xp,loc,lmid):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.constitution = constitution
        self.charisma = charisma
        self.willpower= willpower
        self.maxhealth = (strength + constitution)
        self.temphealth = temphealth
        self.melee = (strength + dexterity) / 2
        self.ranged = (dexterity + intelligence) / 2
        self.defense = (constitution + willpower) / 2
        self.magic = (intelligence + willpower) / 2
        self.xp = xp
        self.location = loc
        self.lastMessageID = lmid
        
    def getStats(self):
        return {
            "name":self.name,
            "Str":self.strength,
            "Dex":self.dexterity,
            "Int":self.intelligence,
            "Con":self.constitution,
            "Cha":self.charisma,
            "Wil":self.willpower,
            "tempHP":self.temphealth,
            "XP":self.xp,
            "Loc":self.location,
            "lmid":self.lastMessageID
            }

    def __init__(self,ID):
        self.ID = ID

        try:
            #load existing data
            tempData = json.loads(open(f"playerData/{self.ID}.json", "r").read())
            self.createStats(tempData["name"],
                             tempData["Str"],
                             tempData["Dex"],
                             tempData["Int"],
                             tempData["Con"],
                             tempData["Cha"],
                             tempData["Wil"],
                             tempData["tempHP"],
                             tempData["XP"],
                             tempData["Loc"],
                             tempData["lmid"])
        except:
            print(f"Createt Player-data:{self.ID}")
            self.createStats(None,10,10,10,10,10,10,10,None,None,None)
            # muss Antwortconzept ausdenken. mabye mit erwarteAntwort = True/False

    def saveData(self):
        player = (open(f"playerData/{self.ID}.json", "w"))
        writeOutdata = self.getStats()
        player.write(json.dumps(writeOutdata, indent=4))
        player.close()

    def decreaseHP(self,damage):
        damage=damage-self.defense
        if damage > 0:
            return self.health-damage
        elif damage <= 0:
            return self.health

class World:
    
    def __init__(self):
        self.json = json.loads(open(f"game/world.json","r").read())

    def saveData(self):
        world = (open(f"game/world.json","w"))
        writeOutdata = json.dumps(self.json, indent=4)
        world.write(writeOutdata)
        world.close()
    
    def surroundings(self,playerlocation,playerID):
        if self.json[playerlocation]["player"] == []:return"no Player"
        
        #Playerlist
        clearlist=[]
        for x in self.json[playerlocation]["player"]:
            clearlist.append(f"{x}")
        clearlist.remove(str(playerID))

        #Playerlist(names)
        playerlist=[]
        for x in clearlist:
            enemy =json.loads(open(f"playerData/{x}.json","r").read())
            playerlist.append(enemy["name"])
        
        #NPC
        npclist=[]
        for x in self.json[playerlocation]["npc"]:
            npclist.append(x)

        #all
        alle=playerlist+npclist
        surroundings={"player":clearlist,"playernames":playerlist,"npc":npclist,"all":alle}

        return surroundings


#PLAYER-ID-SEARCH
def test():
    test = Player(input("playerID:"))
    print(test.getStats())
    test.saveData()