import turtle




#methoden

def char_create():
    a = input("Willkommen\nBist du das erste mal hier?(y/n)")

    if a == "n":
        try:
            player = (open("playerdata/"+input("Wie heißt du?\n"), "r").read()).split(";")
            print("Wilkommen zurück "+player[0])
        except:
            print("no player found -> exit game")
            exit()
    
    #char_creation    
    elif a == "y":
        a = input("Willst du einen neuen Charakter erstellen? (y/n)")
        if a == "y":
            name = input("wie heißt du?\n")
            #class
            a = input("welche Klasse möchtest du spielen?\n1.Ritter\n2.Mage\n")
            if a == "1":
                klasse = "Ritter"
                str = "3"
                int = "1"
                hp = "5"
            elif a == "2":
                klasse = "Mage"
                str = "1"
                int = "3"
                hp = "5"

            #char_datei erstellen
            player = (open("playerdata/"+name, "w"))
            player.write(name+";"+klasse+";"+str+";"+int+";"+hp)
            player.close()

            #char_datei einlesen
            player = (open("playerdata/"+name, "r").read()).split(";")
            print("Wilkommen "+player[0])

            
        else:
            print("exit game")
            exit()
    
    return player

def status(player):
    print("\nStatus:")
    playerstruktur = ['name','class','str','int','hp']
    i = 0
    for x in playerstruktur:
        print(x+"\t:\t",player[i])
        i=i+1
#playerstruktur:['name','class','str','int','hp']


# Start

game = True

player = char_create()
status(player)


# todo: Maingameloop


            
    


    

while game == True:
    break
    


# textsammlung





