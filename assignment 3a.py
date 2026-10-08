# Narang, Arjun
# Computer Progaming, Period 4
# Assignment: Homework 4
# October 7, 2026
alienColor = ("green")
if alienColor == "green":
    print ("you earned 5 points")
else:
    print ("you got 10 points")

alienColor = ("yellow")
if alienColor == "green":
    print ("you earned 5 points")
else:
    print ("you got 10 points")

alien = "green"
if alien == "green":
    print ("You have earned 5 points")
elif alien == "yellow":
    print ("You earned 10 points")
else:
    print ("You earned 15 points")

alien = "yellow"
if alien == "green":
    print ("You have earned 5 points")
elif alien == "yellow":
    print ("You earned 10 points")
else:
    print ("You earned 15 points")

alien = "red"
if alien == "green":
    print ("You have earned 5 points")
elif alien == "yellow":
    print ("You earned 10 points")
else:
    print ("You earned 15 points")

age = int(input("Please input your age"))
if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")

usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ["john", "sarah", "mike", "admin", "alex"]
new_users = ["JOHN", "mike", "david", "chris", "LAUREN"]
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} is already taken. You will need to enter a new username.")
    else:
        print(f"The username {new_user} is available!")

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        ending = "st"
    elif number == 2:
        ending = "nd"
    elif number == 3:
        ending = "rd"
    else:
        ending = "th"
    
    print(f"{number}{ending}")