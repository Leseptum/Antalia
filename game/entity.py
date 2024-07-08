class Player:
    def __init__(self,strength,dexterity,intelligence,endurance,charisma,willpower):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.endurance = endurance
        self.charisma = charisma
        self.willpower= willpower
        self.health = (strength + endurance)
        self.melee = (strength + dexterity) / 2
        self.ranged = (dexterity + intelligence) / 2
        self.defense = (endurance + willpower) / 2
        self.magic = (intelligence + willpower) / 2
        self.xp = 0
        self.location = None

    def getStats(self):
        return {"Stärke":self.strength,"Geschicklichkeit":self.dexterity,"Intelligenz":self.intelligence,"Ausdauer":self.endurance,"Charisma":self.charisma,"Willenskraft":self.willpower,"Leben":self.health,"Nahkampf":self.melee,"Fernkampf":self.ranged, "Verteidigung":self.defense, "Magic":self.magic,"XP":self.xp,"Ort":self.location}

    def getHurt(self,damage):
        damage=damage-self.defense
        if damage > 0:
            return self.health-damage
        elif damage <= 0:
            return self.health

    
