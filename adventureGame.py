# 30 if statements 
firstDirection = input("Would you like to turn right or life")
if firstDirection == "left":
    print ("you have endtered a haunted house.")
    print ("you hear sounds. You see hallway. And there are stairs.")
    x = input("pick which to follow: \na for follow the sounds \nb for down the hallway\n c walk up the stairs")
elif firstDirection == "right":
    print("Your dead you got hit by a car.")
if x == "a":
    print ("A giant spide jumps out at you and spits acid on you and you die.")
elif x == "b":
    print ("You walk down the hall way and as you enter a room the floor board and you fall into a whole and die of starvation.")
else: 
    print ("You walk up the stairs to see a empty room witht he door wide open")
    y = input("do you go in. \n yes\n no").lower ()
if x == "no":
    print ("You choose to leave the house and the adventure ends.")
else:
    print ("You walk into a room to see a body on the table and robots surounding you off. This stuff looks like it hasnt been touched in years but the technology is reallly advanced. You see a button infront of a tank.")

