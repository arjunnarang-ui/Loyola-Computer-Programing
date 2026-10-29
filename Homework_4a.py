Person = {"name":"Dolly",
          "lastName":"Narang",
          "age":45,
          "City":"Redondo Beach"}
aboutMe = {"name":"Rafie",
           "age":"16",
           "favFood":"sushi",
           "haircolor":"brown",
           "favSubject":"Math",
           "favSweet":"pie",
           "favHobbies":"Golf",
           "likeCoding":False
           }

print (aboutMe)

phoneBook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phoneBook["Jake"] = 999879096
phoneBook["Jill"] = 938273443

GlossaryOfHistory = {"YAWAHI":"God",
                     "Solidarty": "Standing with others",
                     "indubatably":"yes or correcy",
                     "puella":"girl",
                     "liquatious":"talkative"}

print("YAWAHI:\n\t" + GlossaryOfHistory["YAWAHI"])
print("Solidarty:\n\t" + GlossaryOfHistory["Solidarty"])
print("indubatably:\n\t" + GlossaryOfHistory["indubatably"])
print("puella:\n\t" + GlossaryOfHistory["puella"])
print("liquatious:\n\t" + GlossaryOfHistory["liquatious"])

GlossaryOfHistory["democracy"] = "A system of government by the whole population"
GlossaryOfHistory["dynasty"] = "A line of hereditary rulers of a country"
GlossaryOfHistory["monarchy"] = "A form of government with a monarch at the head"
GlossaryOfHistory["senate"] = "Any of various legislative or governing bodies"
for k, v in GlossaryOfHistory.items():
    print(k, v)

# Create the dictionary with three major rivers and their countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print() # empty line for spacing
print("Rivers:")
for river in rivers.keys():
    print(river.title())
print() 
print("Countries:")
for country in rivers.values():
    print(country.title())


person1 = {
    "first name": "bob",
    "last name": "jones",
    "fav_color": "blue",
    "birth month": "march"}
person2 = {
    "first name": "bobby",
    "last name": "jonessss",
    "fav_color": "red",
    "birth month": "april"}
person3 = {
    "first name": "rob",
    "last name": "jo",
    "fav_color": "purple",
    "birth month": "december"}
people = [person1, person2, person3]
for p in people:
    print(
        "Name: " + p["first name"].title() + " " + p["last name"].title() + 
        ", Favorite Color: " + p["fav_color"].title() + 
        ", Birth Month: " + p["birth month"].title())

cities = {
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "It is the most populous metropolitan area in the world.",},
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Known as the City of Light.",},
    "cairo": {
        "country": "egypt",
        "population": "10 million",
        "fact": "It is set on the Nile River.",},
}
for city_name, info in cities.items():
    print("City: " + city_name.title())
    print("\tCountry: " + info["country"].title())
    print("\tPopulation: " + info["population"])
    print("\tFact: " + info["fact"] + "\n")
