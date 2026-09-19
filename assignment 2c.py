#Arjun Narang
#Period 4
#9/18/2026

#set up the flight log variable.
flightLog = [1000, 2500, 4200, 6000, 7800, 9500, 11000, 12500]
print (flightLog)
#adding numbers to the end of the flight log variable.
flightLog.append (12550)
flightLog.append (12551)
print (flightLog)
#removing a number in the variable through pop.
flightLog.pop (1)
flightLog.pop (-1)
print (flightLog)
# inserting a new number into a specific point in the flight log.
flightLog.insert (1, 4100)
print (flightLog)
#Printing the f string with a sentence using the flightlog variable.
print (f"The flight log states that at the hight of {flightLog [2]}ft it was 2pm.")