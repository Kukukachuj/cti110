modual_grades = []
mod1grade = float(input('Enter grade for Module 1:'))
mod2grade = float(input('Enter grade for Module 2:'))
mod3grade = float(input('Enter grade for Module 3:'))
mod4grade = float(input('Enter grade for Module 4:'))
mod5grade = float(input('Enter grade for Module 5:'))
mod6grade = float(input('Enter grade for Module 6:'))
modual_grades.append(mod1grade)
modual_grades.append(mod2grade)
modual_grades.append(mod3grade)
modual_grades.append(mod4grade)
modual_grades.append(mod5grade)
modual_grades.append(mod6grade)

average = round(sum(modual_grades) / len(modual_grades), 2)

print('------------Results------------')
print(f'Lowest Grade:       {min(modual_grades)}')
print(f'Highest Grade:      {max(modual_grades)}')
print(f'Sum of Grades:      {sum(modual_grades)}')
print(f'Average:            {average:.2f}')
print('----------------------------------------')


