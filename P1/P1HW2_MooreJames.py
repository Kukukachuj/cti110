

budget=int(input("Enter the budget:"))  #Users Total Budget Input
destination=input("Enter Your destination:")  #Users Desintaion Input
fuel=float(input("Enter amount that you will spend on gas:"))  #Users Gas Expenses Input
accomodation=float(input("Enter amount that you will spend on accomodation:")) #User Accomodation Input
food=float(input("Enter amount that you will spend on food:")) #Users Food Expenses Input
expenses=fuel+accomodation+food #Addintion of all Expenses  
print("----------------Travel Exspenses-----------------") 
print("Location: ",destination)
print("initial Budget: ",budget)
print (end='')
print("fuel: ",fuel)
print("Accomodations: ",accomodation)
print("Food: ",food)
print(end='')
print("Remaining Balance: ",budget-expenses)