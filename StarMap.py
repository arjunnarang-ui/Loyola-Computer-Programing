# Arjun Narang
# November 3, 2026 
# Digital Star Map 


# Part 1: Build the Database
stars = {
    "Sun": {"x": 0, "y": 0, "z": 0, "luminosity": 1.0, "mass": 1.0},
    "Sirius": {"x": -1.6, "y": 8.1, "z": -2.5, "luminosity": 25.4, "mass": 2.06},
    "Vega": {"x": 7.2, "y": -4.5, "z": 25.3, "luminosity": 40.0, "mass": 2.14},
    "Proxima Centauri": {"x": 1.6, "y": -3.8, "z": -1.2, "luminosity": 0.0017, "mass": 0.12},
    "Betelgeuse": {"x": 88.0, "y": -120.0, "z": 45.0, "luminosity": 100000.0, "mass": 16.5}
}

print(len(stars))
print(stars["Sirius"]["mass"])
print(f"Vega is at ({stars['Vega']['x']}, {stars['Vega']['y']}, {stars['Vega']['z']})")


# Part 2: Loop and Finding the Average Mass
totalMass = 0
for name in stars:
    m = stars[name]["mass"]
    lum = stars[name]["luminosity"]
    print(f"{name}: mass {m}, luminosity {lum}")
    totalMass += m

averageMass = totalMass / len(stars)
print("Average mass:", averageMass)

brightestStar = ""
maxLum = -1.0
for name in stars:
    if stars[name]["luminosity"] > maxLum:
        maxLum = stars[name]["luminosity"]
        brightestStar = name

print("Brightest star:", brightestStar)


# Part 3: Search and Updaate the Map
searchInput = input("Enter star to look up: ").strip().title()

if searchInput in stars:
    print(stars[searchInput])
else:
    print("Star not found")

stars["Proxima Centauri"]["mass"] = 0.122
stars["Polaris"] = {"x": 0.0, "y": 433.0, "z": 0.0, "luminosity": 1260.0, "mass": 5.4}

del stars["Sun"]
print(len(stars))

totalMass2 = 0
for name in stars:
    totalMass2 += stars[name]["mass"]

newAverageMass = totalMass2 / len(stars)
print("New average mass:", newAverageMass)


# Part 4: Obsvation Log a List of Dictionaries
observationLog = [
    {"star": "Sirius", "night": 1, "clear_sky": True},
    {"star": "Vega", "night": 2, "clear_sky": True},
    {"star": "Betelgeuse", "night": 3, "clear_sky": False}
]

for entry in observationLog:
    sName = entry["star"]
    print(f"Night {entry['night']}: {sName} (clear sky: {entry['clear_sky']})")
    print(stars[sName]["mass"])

newLogStar = input("Enter another star name for log: ").strip().title()
newLogEntry = {"star": newLogStar, "night": 4, "clear_sky": True}
observationLog.append(newLogEntry)
print(len(observationLog))