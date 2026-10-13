# 30 if statements 
firstDirection = input("Would you like to turn right or left: ")
if firstDirection == "left":
    print ("you have endtered a haunted house.")
    print ("you hear sounds. You see hallway. And there are stairs.")
    x = input("pick which to follow: \na for follow the sounds \nb for down the hallway\nc walk up the stairs: ")
    if x == "a":
        print ("A giant spide jumps out at you and spits acid on you and you die.")
    elif x == "b":
        print ("You walk down the hall way and as you enter a room the floor board and you fall into a whole and die of starvation.")
    else: 
        print ("You walk up the stairs to see a empty room witht the door wide open")
        y = input("do you go in: ").lower ()
        if y == "no":
            print ("You go home safe and sound.")
        else:
            print ("all of a sudden an eagle swoops in through the window and carries you away further and furth from the house")
            z= input("You start to slip do you let go or try to hold on to the bird. \na for hold on \nb to let go: ")
            if z == "a":
                print ("the bird and you slowly fall to both your deaths")
            else: 
                print ("you end up letting go and as you fall you land one a plane. You look across the plane and you spiderman and Ironman fighting who do you help.")
                q = input ("who do you help. \nspiderman \nironman: ")
                if q == "spiderman":
                    print ("You charge at iron man with all your might and he just blasts you in the face and you die")
                else:
                    print ("You ride on ironmans soldier and he throws you at spiderman and spiderman falls to his death you land on top of him so you survive.")
                    w = input("your in the middle of the dessert now do you walk forwards or backwards in hopes of water. Choose: \nforward\nbackward: ")
                    if w == "backward":
                        print ("you keep searchign for water and eventually die of thirst")
                    else:
                        print ("you end up finding a bar in villiage which feeds you give you water and nurses you back to health.")
                        e = input ("when u wake up do u \na pay them back for their hospitality \nb dont pay them or say thank you and run away: ")
                        if e == "a":
                            print ("they thank you and you leave but while leaving some people come to mug you and since you dont have anymore money to give you die.")
                        else: 
                            print ("you run out the bar. As you runing you stumble apon an acient temple.")
                            r = input("Do you go in the temple \na yes \nb no: ")
                            if r == "b":
                                print ("you sit outside the temple until night time and a jaguar eats you.")
                            else:
                                print ("you walk into the temple and find two golden levers.")
                                t = input("do you pull \na left lever \nb right lever: ")
                                if t == "a":
                                    print ("the floor opens up and poison darts shoot you and you die.")
                                else:
                                    print ("a hidden wall slides open showing a shiny crown and a magical sword.")
                                    u = input("do you pick up \na crown \nb sword: ")
                                    if u == "a":
                                        print ("the crown is cursed and turns you into stone instantly.")
                                    else:
                                        print ("you grab the sword and a giant stone guard comes alive to attack you.")
                                        i = input("do you \na fight the guard \nb run deeper into the temple: ")
                                        if i == "a":
                                            print ("your sword bounces off his armor and he squashes you.")
                                        else:
                                            print ("you escape into a room with a magical teleportation portal.")
                                            o = input("do you step in the portal \na yes \nb no: ")
                                            if o == "b":
                                                print ("the temple crumbles down on top of you and you die.")
                                            else:
                                                print ("you teleport into a dark cave with a sleeping dragon.")
                                                p = input("do you \na sneak past the dragon \nb attack the dragon: ")
                                                if p == "b":
                                                    print ("the dragon wakes up and burns you to ashes.")
                                                else:
                                                    print ("you sneak past and find a treasure chest filled with gold.")
                                                    a_choice = input("do you open the chest \na yes \nb no: ")
                                                    if a_choice == "b":
                                                        print ("you walk past it into a trap and fall down a pit.")
                                                    else:
                                                        print ("you open the chest and get rich and escape the cave alive and win the game!")

elif firstDirection == "right":
    print("Your dead you got hit by a car.")
