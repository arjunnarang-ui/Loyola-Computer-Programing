# Narang, Arjun
# Computer Programming, period 4
# Assignment: Homework 7
# November 20, 2026

def make_shirt(size, message):
    print ("The shirt size is " + size + " and the message on it is " + message)

make_shirt("medium", "Go Loyola")
make_shirt(size="large", message="Python Rules")

def make_shirt2(size="large", message="I love Python"):
    print ("The shirt size is " + size + " and the message on it is " + message)

make_shirt2()
make_shirt2(size="medium")
make_shirt2(size="small", message="Coding is fun")

def describe_city(city, country="United States"):
    print (city + " is in " + country)

describe_city("Los Angeles")
describe_city("New York")
describe_city("Reykjavik", "Iceland")

def city_country(city, country):
    return city + ", " + country

print (city_country("Santiago", "Chile"))
print (city_country("Tokyo", "Japan"))
print (city_country("Paris", "France"))

def make_album(artist, title, numSongs=None):
    albumInfo = {"artist": artist, "title": title}
    if numSongs:
        albumInfo["num_songs"] = numSongs
    return albumInfo

print (make_album("J. Cole", "2014 Forest Hills Drive"))
print (make_album("Frank Ocean", "Blonde"))
print (make_album("Travis Scott", "Astroworld"))
print (make_album("Kendrick Lamar", "DAMN.", numSongs=14))

while True:
    artistInput = input("Enter album artist (or 'quit' to stop): ")
    if artistInput == "quit":
        break
    titleInput = input("Enter album title (or 'quit' to stop): ")
    if titleInput == "quit":
        break
    print (make_album(artistInput, titleInput))

myMessages = ["Hey, how are you?", "On my way!", "See you soon."]

def show_messages(msgList):
    for msg in msgList:
        print (msg)

show_messages(myMessages)

myMessages = ["Hey, how are you?", "On my way!", "See you soon."]
sentMessages = []

def send_messages(msgList, sentList):
    while msgList:
        currentMsg = msgList.pop(0)
        print (currentMsg)
        sentList.append(currentMsg)

send_messages(myMessages, sentMessages)
print (myMessages)
print (sentMessages)

myMessages = ["Hey, how are you?", "On my way!", "See you soon."]
sentMessages = []

send_messages(myMessages[:], sentMessages)
print (myMessages)
print (sentMessages)

def make_sandwich(*sandwichItems):
    print ("Making a sandwich with:")
    for item in sandwichItems:
        print (item)

make_sandwich("turkey")
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("roast beef", "cheddar", "tomato", "mayo", "pickles")

def make_car(manufacturer, model, **carInfo):
    carInfo["manufacturer"] = manufacturer
    carInfo["model"] = model
    return carInfo

myCar = make_car("subaru", "outback", color="blue", tow_package=True)
print (myCar)

import shirt_functions
shirt_functions.make_shirt("large", "Import 1")

from shirt_functions import make_shirt
make_shirt("medium", "Import 2")

from shirt_functions import make_shirt as fn
fn("small", "Import 3")

import shirt_functions as mn
mn.make_shirt("extra large", "Import 4")

from shirt_functions import *
make_shirt("medium", "Import 5")