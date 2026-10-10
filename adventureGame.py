# 30 if statements 
firstDirection = input("Would you like to turn right or life")
if firstDirection == "left":
    print ("you have endtered a haunted house.")
    print ("you hear sounds. You see hallway. And there are stairs.")
    x = input("pick which to follow: \na for follow the sounds \nb for down the hallway\n c walk up the stairs")
    if x == "a":
        print ("A giant spide jumps out at you and spits acid on you and you die.")
    elif x == "b":
        print ("You walk down the hall way and as you enter a room the floor board and you fall into a whole and die of starvation.")
    else: 
        print ("You walk up the stairs to see a empty room witht the door wide open")
        y = input("do you go in. \n yes\n no").lower ()
        if y == "n":
            print ("You go home safe and sound.")
        else:
            print ("all of a sudden an eagle swoops in through the window and carries you away further and furth from the house")
            z= input("You start to slip do you let go or try to hold on to the bird. \n a for hold on \n b to let go")
            if z == "a":
                print ("the bird and you slowly fall to both your deaths")
            else: 
                print ("you end up letting go and as you fall you land one a plane. You look across the plane and you spiderman and Ironman fighting who do you help.")
                q = input ("who do you help. \nspiderman \nironman")
                if q == "spiderman":
                    print ("You charge at iron man with all your might and he just blasts you in the face and you die")
                else:
                    print ("You ride on ironmans soldier and he throws you at spiderman and spiderman falls to his death you land on top of him so you survive.")
                    w = input("your in the middle of the dessert now do you walk forwards or backwards in hopes of water. Choose: \nforward\nbackward")
                    if w = "backward":
                        print ("you keep searchign for water and eventually die of thirst")
                    else:
                        print ("you end up finding a bar in villiage which feeds you give you water and nurses you back to health.")
                        e = input ("when u wake up do u a \npay them back for their hospitality \b dont pay them or say thank you and run away.")
                        if e == a:
                            print ("they thank you and you leave but while leaving some people come to mug you and since you dont have anymore money to give you die.")
                        else: 
                            print ("you run out the bar. As you runing you stumble apon an acient temple.")
                            r == input("Do you go in the temple \a yes \b no")


    
elif firstDirection == "right":
    print("Your dead you got hit by a car.")

