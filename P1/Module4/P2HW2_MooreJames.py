# CTI-110
# P2HW2 - List
# James Moore
# 03/9/2023
# Whats Your Average

module_grades = [] #Empty list to store user values 
mod1grade = float(input('Enter grade for Module 1: '))  #Users Module 1 grade input
mod2grade = float(input('Enter grade for Module 2: '))  #Users Module 2 grade input
mod3grade = float(input('Enter grade for Module 3: '))  #Users Module 3 grade input
mod4grade = float(input('Enter grade for Module 4: '))  #Users Module 4 grade input
mod5grade = float(input('Enter grade for Module 5: '))  #Users Module 5 grade input
mod6grade = float(input('Enter grade for Module 6: '))  #Users Module 6 grade input
module_grades.append(mod1grade)                        #Adds module 1 grade to module_grades list
module_grades.append(mod2grade)                        #Adds module 2 grade to end of module_grades list
module_grades.append(mod3grade)                        #Adds module 3 grade to end of module_grades list
module_grades.append(mod4grade)                        #Adds module 4 grade to end of module_grades list
module_grades.append(mod5grade)                        #Adds module 5 grade to end of module_grades list
module_grades.append(mod6grade)                        #Adds module 6 grade to end of module_grades list

average = round(sum(module_grades) / len(module_grades), 2) 
#Calculates the average of module_list items by deviding the sum of module_grades by the number of items 
#in the and rounds up 2 decimal places and stores value as 'average'

print('------------Results------------')               #Displays top bar
print(f'Lowest Grade:       {min(module_grades)}')     #Displays the lowest grade in the list
print(f'Highest Grade:      {max(module_grades)}')     #Displays the highest grade in list
print(f'Sum of Grades:      {sum(module_grades)}')     #Displays the sum of list items
print(f'Average:            {average:.2f}')            #Displays the value of 'Average'
print('----------------------------------------')      #Displays bottom Bar


