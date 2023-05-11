# Random Number Math Quiz
# 05/09/23
# CTI-110 P5HW - Math Quiz 
# James Moore
 
import random

def add():                       #Addition Function
    a = random.randint(1,100)
    b = random.randint(1,100)    #Gets random numbers   
    print("   ",a)
    print(" + ",b)                  
    print('------')
    sum = a+b
    ans = int(input("Enter answer: "))  
    guess = 1                    #Var for guesses
    
    while sum!=ans:                #Loop for incorrect answer
        if ans<sum:                 #Answer to low 
            print("Guess is too low.") 
        else:                        #Anser to high   
            print("Guess is too high.")
        ans = int(input("\ntry again: "))
        guess+=1
    print("Your answer is correct!")
    print("Number of guesses: ",guess)

def subtract():             #Function for Subtraction
    a = random.randint(1, 100)  #Gets random numbers
    b = random.randint(1, 100)
    print("   ", a)
    print(" - ", b)
    print('------')
    diffrence = a - b
    ans = int(input("Enter answer: "))
    guess = 1
    
    while diffrence != ans:    #Loop for incorrect answer
        if ans < diffrence:     #Answer to low
            print("Guess is too low.")
        else:                   #answe to high
            print("Guess is too high.")
        ans = int(input("\ntry again: "))
        guess += 1              #Guess add 1
    print("Your answer is correct....")
    print("Number of guesses: ", guess)

def menu():         #Function for menu
    print("\nMain Menu")
    print("-"*15)
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit\n")
    option = int(input("Please choose one of the option: "))
    if option==1:   #Goes to add funtion
        add()
    elif option==2: #goes to subtract funtion
        subtract()
    elif option == 3:   #Exits 
        print("Bye!!")
        exit()
    else:                       
        print("Invalid, Please choose again")
    menu()
    
print("Welcome To My Math Quiz\n")
menu()