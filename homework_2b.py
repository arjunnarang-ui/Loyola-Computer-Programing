#Arjun Narang
#Period 4
#Assignment 2b
# September 25, 2026
alien_color = 'green'
if alien_color == 'green':                     
    print("You earned 5 points for shooting the alien!")
else:                                         
    print("You earned 10 points!")
alien_color = 'yellow'
if alien_color == 'green':                     
    print("You earned 5 points for shooting the alien!")
else:                                         
    print("You earned 10 points!")
alien_color = 'green'
if alien_color == 'green':                     
    print(" You earned 5 points!")
elif alien_color == 'yellow':                   
    print(" You earned 10 points!")
else:                                         
    print(" You earned 15 points!")
alien_color = 'yellow'
if alien_color == 'green':                     
    print(" You earned 5 points!")
elif alien_color == 'yellow':                   
    print(" You earned 10 points!")
else:                                         
    print(" You earned 15 points!")
alien_color = 'red'
if alien_color == 'green':                     
    print(" You earned 5 points!")
elif alien_color == 'yellow':                   
    print(" You earned 10 points!")
else:                                         
    print(" You earned 15 points!")
ages = [1, 3.9, 10, 13, 19, 20, 21, 65]
for age in ages:                               
    if age < 2:                                
        print(f"Age {age}: Person is a baby.")
    elif age < 4:                              
        print(f"Age {age}: Person is a toddler.")
    elif age < 13:                             
        print(f"Age {age}: Person is a kid.")
    elif age < 20:                             
        print(f"Age {age}: Person is a teenager.")
    elif age < 65:                             
        print(f"Age {age}: Person is an adult.")
    else:                                      
        print(f"Age {age}: Person is an elder.")
usernames = ['admin', 'jaden', 'arjun', 'sarah', 'alex']
if len(usernames) > 0:                        
    for username in usernames:
        if username == 'admin':                 
            print("Hello admin, would you like to see a status report?")
        else:                                
            print(f"Hello {username.title()}, thank you for logging in again.") # .title() from notes
else:
    print("We need to find some users!")
# Testing with an empty list
usernames = []
if len(usernames) > 0:                         
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:                                  # Added 'else' (not in notes)
            print(f"Hello {username.title()}, thank you for logging in again.")
else:                                          # Added 'else' (not in notes)
    print("We need to find some users!")
current_users = ['john', 'sarah', 'arjun', 'admin', 'mike']
new_users = ['JOHN', 'mary', 'Arjun', 'david', 'alex']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())   # .append() and .lower() from notes
for new_user in new_users:
    if new_user.lower() in current_users_lower: # Added 'if' and 'in' operator (not in notes)
        print(f"The username '{new_user}' is already taken. You will need to enter a new username.")
    else:                                      # Added 'else' (not in notes)
        print(f"The username '{new_user}' is available.")
numbers = list(range(1, 10))                   
for num in numbers:
    if num == 1:                               
         print(f"{num}st")
    elif num == 2:                             
        print(f"{num}nd")
    elif num == 3:                            
        print(f"{num}rd")
    else:                                      
        print(f"{num}th")