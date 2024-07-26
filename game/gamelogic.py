import entity,json

def getText(message):
    storydata = json.loads(open(f"game/text.json", "r").read())
    player=entity.Player(message.author.id)
    player.saveData()    
    
    if message.content == "$hello":
        if player.name == None:
            player.lastMessageID = "name"
            player.saveData()
            return "Hi\nWie heißt du?"
        else:
            return f"Hallo {player.name}"
        
    if player.lastMessageID == "name":
        player.name = message.content[1:]
        player.lastMessageID = "0"
        player.saveData()
        return f"hello {player.name},to play $s1"
    
    #befehle
    if message.content == "$stats":
        return f"{player.getStats()}"
    
    #Story
    if message.content.startswith('$s'):
        try: 
            exportdata = storydata[player.lastMessageID]["text"]
            player.location = storydata[player.lastMessageID]["Location"]
            player.lastMessageID = storydata[player.lastMessageID]["Antworten"][message.content[2:]]
            player.saveData()
            return exportdata
        except: return "failed:no_dict"

#print("\n".join("{}\t{}".format(k, v) for k, v in storydata.items()))
#print((storydata["0"]["Antworten"]["2"]))
