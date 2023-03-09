user_name = input()
print ('Hello',user_name,'and welcome to CS Online!')
Budget = float(input ("What is yout budget?"))
Destination = input ("What is your travel destination?")
Gas = float(input ("How much will you spend on gas?"))
Accom = float(input ("What about accommodations?"))
Food = float(input ("And Food?"))
Ex = Gas+Food+Accom 
print ("Your total exspenses = $",Ex)
TtlEx = Budget - Ex
print("You will have $",TtlEx,"left in your budget.") 