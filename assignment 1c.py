#Arjun Narang
#assignment 1c
nameOfObject = input("Enter the name of the object:")
massKg = input ("what is the mass of the object in kg?")
velocity = input ("what is the velocity of the object in m/s")

nameOfObjectClean = nameOfObject.strip().title()
massKgNum = float (massKg)
velocityNum = float(velocity)
KEJoules= 1/2*massKgNum*velocityNum**2
KECalories = KEJoules/4.184
KEErgs = KEJoules * 10**7
print ("Kinetic Energy Report for:", nameOfObjectClean)
outputLineOne = f"Kinetic Energy Report for:" {nameOfObjectClean}
print (outputLineOne)
print ("-----------------------------------------------------")
outputLineThree = f"Joules:\t{KEJoules} J"
print (outputLineThree)