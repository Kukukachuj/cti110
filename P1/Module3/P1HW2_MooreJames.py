#A program that takes in a users Trip exspenses and budget and displays them while subtracting the exspenses from thier budget. 
#Date 02-12-2023
#CTI-110P1HW2 - Travel Expsense 
# James Moore
budget=int(input("Enter the budget:"))  #Users Total Budget Input
destination=input("Enter Your destination:")  #Users Desintaion Input``
fuel=int(input("Enter amount that you will spend on gas:"))  #Users Gas Expenses Input
accomodation=int(input("Enter amount that you will spend on accomodation:")) #User Accomodation Input
food=int(input("Enter amount that you will spend on food:")) #Users Food Expenses Input
expenses=fuel+accomodation+food #Addintion of all Expenses  
print("----------------Travel Exspenses-----------------") #Prints Title bar
print("Location:",destination) #Prints User Location
print("Initial Budget:",budget) #Prints Starting Budget
print ("") #Skips Line
print("Fuel: ",fuel)#Prints fuel costs
print("Accomodations:",accomodation)#Prints accomodations
print("Food:",food)#Prints food costs
print("")#Skips line
print("Remaining Balance:",budget-expenses)#Prints Remaining balance 