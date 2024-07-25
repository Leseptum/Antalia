import entity,json

storydata = json.loads(open(f"game/text.json", "r").read())


def getText(message):
    player=entity.Player(message.author.id)
    player.saveData()    
    if player.lastMessageID == None:
        player.lastMessageID = 1
        player.saveData()
        return "Wie heißt du?"
    if player.lastMessageID == 1:
        player.name = message.content[1:]
        player.lastMessageID = 2
        player.saveData()
        return f"hello {player.name}"
    if player.lastMessageID == 2:
        return f"{player.getStats()}"