import entity,json

try:
    storydata = json.loads(open(f"game/text.json", "r").read())
    print("loaded Storydata")
except:print("failed to load Storydata")



def getText(message):
    player=entity.Player(message.author.id)
    player.saveData()    
    world = entity.World()

    if message.content == "$hello":
        if player.name == None:
            player.lastMessageID = "name"
            player.saveData()
            return "Hallo\nWie heißt du?"
        else:
            return f"Hallo {player.name}"
        
    if player.lastMessageID == "name":
        player.name = message.content[1:]
        player.lastMessageID = "0"
        player.lvl = 1
        player.location = "Erlotan Umland"
        world.json[player.location]["player"].append(str(player.ID))
        player.saveData()
        world.saveData()
        return f"hello {player.name}, enter $m"
    
    #befehle
    if message.content == "$":return"""
    available Commands:
    $       :  available Commands
    $hello  :  Start your Adventure and just say hello
    $stats  :  Get your stats
    $m[]    :  move to the next available location (bsp: $mErlotan)
    $m      :  show what is around you
    """
    if message.content == "$stats": return f"{player.getStats()}"
    
    if message.content.startswith('$m'):
        if player.name == None:return "enter $hello or $"
        returnwert = f"Du bist an folgendem Ort: {player.location}\nDu kannst folgende Orte erreichen{world.json[player.location]["reachable"]}\nUm dich herrum sind:{world.surroundings(player.location,player.ID)["all"]}"

        if message.content == "$m":return returnwert

        if message.content[2:] in world.json[player.location]["reachable"]:
            if str(player.ID) in world.json[player.location]["player"]:
                world.json[player.location]["player"].remove(str(player.ID))
                world.json[message.content[2:]]["player"].append(str(player.ID))
                world.saveData()
                player.location = message.content[2:]
                player.saveData()
            return returnwert
        else:return "diesen Ort kannst du nicht erreichen"

    if message.content.startswith('$f'):
        if player.name == None:return "enter $hello or $"
        if message.content == "$f":return f"Um dich herrum sind: {world.surroundings(player.location,player.ID)["all"]}"
        if message.content[2:] in world.surroundings(player.location,player.ID)["all"]:
            return "reachable"
            '''
            if precision >= doge:
                if defence >= damage:hit
        
            '''
            
    else:return "bad read"



'''Auskommentiert

    #Story
    if message.content.startswith('$s'):
        if message.content == "$s": return storydata[player.lastMessageID]["text"]
        try: 
            player.location = storydata[player.lastMessageID]["Location"]
            player.lastMessageID = storydata[player.lastMessageID]["Antworten"][message.content[2:]]
            exportdata = storydata[player.lastMessageID]["text"]
            player.saveData()
            return exportdata
        except: return "failed:no_dict"

        
print("\n".join("{}\t{}".format(k, v) for k, v in storydata.items()))
print((storydata["0"]["Antworten"]["2"]))
'''

