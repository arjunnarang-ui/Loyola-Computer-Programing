# Narang, Arjun
# Computer Programming, period 4
# Assignment: Homework 5a
# November 11, 2026

group_input = float(input("How many people are in your group? "))
if group_input <= 0 or group_input % 1 != 0:
    print("That number does not make sense for a dinner group.")
elif group_input > 8:
    print("Your table is not ready, you have to wait.")
else:
    print("Your table is ready!")

num = float(input("Please enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10!")
else:
    print(f"{num} is not a multiple of 10.")

topping = ""
while topping != "quit":
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza!")

age_input = ""
while age_input != "quit":
    age_input = input("Enter your age (or 'quit' to stop): ")
    if age_input != "quit":
        age = float(age_input)
        if age < 0:
            print("Invalid age! Age cannot be negative.")
        elif age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

active = True
while active:
    age_input = input("Enter your age (or 'quit' to stop): ")
    if age_input == "quit":
        active = False
    else:
        age = float(age_input)
        if age < 0:
            print("Invalid age! Age cannot be negative.")
        elif age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

while True:
    age_input = input("Enter your age (or 'quit' to stop): ")
    if age_input == "quit":
        break
    age = float(age_input)
    if age < 0:
        print("Invalid age! Age cannot be negative.")
    elif age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

sandwich_orders = [
    "tuna",
    "pastrami",
    "turkey",
    "pastrami",
    "ham",
    "roast beef",
    "pastrami",
]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"Finished: {sandwich} sandwich")

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = vacation
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        polling_active = False

for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")