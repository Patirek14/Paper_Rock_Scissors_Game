import time,random
def clear():
    for x in range(300):
        print("")

print("==================HELLO==================")
print("This is a rock paper scissors game , when you ready press any key to continue.")
print("==================HOW TO PLAY==================")
print("To paper press P on keyboard for rock press R for scissors press S")
input()
#clear()
print("3..")
#clear()
time.sleep(1)
print("2..")
#clear()
time.sleep(1)
print("1..")
time.sleep(1)
print("START")
comPoints = 0
playerPoints = 0
while(comPoints < 10 and playerPoints < 10):
    x = input("Your turn !!!: ")
    c = random.randrange(3)
    if c == 0:
        print("Computer choosed paper")
    if c == 1:
        print("Computer choosed rock")
    if c == 2:
        print("Computer choosed scissor")
    if c == 0 and x == "P":
        comPoints = comPoints + 1
        playerPoints = playerPoints+ 1
    elif c == 0 and x == "R":
        comPoints =+ 1
    elif c == 0 and x == "S":
        playerPoints = playerPoints + 1
        ###############
    elif c == 1 and x == "R":
        comPoints = comPoints + 1
        playerPoints = playerPoints + 1
    elif c == 1 and x == "S":
        comPoints = comPoints + 1
    elif c == 1 and x == "P":
        playerPoints = playerPoints + 1
        ###############
    elif c == 2 and x == "S":
        comPoints =  comPoints + 1
        playerPoints = playerPoints + 1
    elif c == 2 and x == "P":
        comPoints =  comPoints + 1
    elif c == 2 and x == "R":
        playerPoints = playerPoints + 1
    print(str(playerPoints) + " : " + str(comPoints))

if playerPoints > comPoints:
    print("PLAYER HAS WON")
elif playerPoints == comPoints:
    print("REMIS")
else:
    print("COMPUTER HAS WON")

  #MADE BY PATIREK 14  
  #THIS IS IN BRANCH "MOBILE"
