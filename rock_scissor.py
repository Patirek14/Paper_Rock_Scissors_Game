import time,random

key_codes = {"paper":"P", "rock":"R", "scissors":"S"}
map_codes = ["paper","rock","scissors"]
init_time = 3

def config_game():
    file = open("config.config")
    line = file.read(1)
    init_time = int(line)
    line = file.read(1)
    key_codes["paper"] = line
    line = file.read(1)
    key_codes["rock"] = line
    line = file.read(1)
    key_codes["scissors"] = line
    #print(key_codes)
    #print(init_time)
def is_key_right(k):
    return k in key_codes.values()
def clear():
    for x in range(300):
        print("")
        
comPoints = 0
playerPoints = 0
config_game()
print("==================HELLO==================")
print("This is a rock paper scissors game , when you ready press any key to continue.")
print("==================HOW TO PLAY==================")
print("To paper press "+ key_codes["paper"] + " on keyboard for rock press "+ key_codes["rock"] + " for scissors press "+ key_codes["scissors"])
input()
for x in range(init_time,0,-1):
    print(str(x) + "...")
    time.sleep(1)
print("START")
while(comPoints < 10 and playerPoints < 10):
    x = input("Your turn !!!: ")
    if(not is_key_right(x)):
        print("Wrong key")
        continue
    c = random.randrange(3)
    print("Computer choosed " + map_codes[c])
    if c == 0 and x == key_codes["paper"]:
        comPoints = comPoints + 1
        playerPoints = playerPoints+ 1
    elif c == 0 and x == key_codes["rock"]:
        comPoints =+ 1
    elif c == 0 and x == key_codes["scissors"]:
        playerPoints = playerPoints + 1
        ###############
    elif c == 1 and x == key_codes["rock"]:
        comPoints = comPoints + 1
        playerPoints = playerPoints + 1
    elif c == 1 and x == "S":
        comPoints = comPoints + 1
    elif c == 1 and x == key_codes["paper"]:
        playerPoints = playerPoints + 1
        ###############
    elif c == 2 and x == key_codes["scissors"]:
        comPoints =  comPoints + 1
        playerPoints = playerPoints + 1
    elif c == 2 and x == key_codes["paper"]:
        comPoints =  comPoints + 1
    elif c == 2 and x == key_codes["rock"]:
        playerPoints = playerPoints + 1
    print(str(playerPoints) + " : " + str(comPoints))

if playerPoints > comPoints:
    print("PLAYER HAS WON")
elif playerPoints == comPoints:
    print("REMIS")
else:
    print("COMPUTER HAS WON")
