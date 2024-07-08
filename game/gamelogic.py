import entity,json

player=open("player.json","r")
print(player.read())


'''
def getText(message):
    if message.content == "$play":
        if str(message.author.id) in player:return "Hello Player"
        else:
            player[str(message.author.id)] = ""
            textfile.write(json.dumps(player))
            return "Welcome"


'''
