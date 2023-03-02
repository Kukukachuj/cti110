#A program that takes in a users Trip exspenses and budget and displays them while subtracting the exspenses from thier budget. 
#Date 02-12-2023
#CTI-110P1HW2 - Travel Expsense 
# James Moore
budget=int(input('Enter the budget:'))  
destination=input('Enter Your destination:')  
fuel=int(input('Enter amount that you will spend on gas:'))  
accomodation=int(input('Enter amount that you will spend on accomodation:')) 
food=int(input('Enter amount that you will spend on food:')) 
expenses=fuel+accomodation+food  
print('----------------Travel Exspenses-----------------') 
print('Location:             ',destination) 
print (f'Initial Budget:        ${budget:.1f}') 
print (f'Fuel:                  ${fuel:.1f}')
print (f'Accomodations:         ${accomodation:.1f}')
print (f'Food:                  ${food:.1f}')
print('-------------------------------------------------')
print('')
print (f'Remaining Balance:     ${budget-expenses:.1f}')
