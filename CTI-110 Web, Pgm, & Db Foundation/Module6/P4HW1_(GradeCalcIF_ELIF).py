# CTI-110
# P2HW2 - List
# James Moore
# 03/9/2023
# Whats Your Average



gradelist =[]        #list
scoreamount = float(input('How many scores do you want?:'))
currentg = 0
while(True):                        # Start of loop 
    while scoreamount > currentg:   # loops until number of scores are entered 
        score = float(input(f'Enter score #{currentg+1} '))
        
        while(True):
            if score < 0 or score > 100: # Stops user entering a number outside of 1-100 and returns error message
                print('INVALID Score entered!!!!\nScore should be between 0 and 100')
                score = int(input(f'Enter score #{currentg+1} again:'))
            else:
                gradelist.append(score)     #if score is valid its added to the list
            break
        currentg+=1
    if currentg == scoreamount: #Breaks loop if number of scores are reached
        break
         
average = round(sum(gradelist) / len(gradelist), 2)  #Gets average of scores in list

if(average>=93 and average<=100):        #|
    grade = 'A'                          #|         
elif(average>=83 and average<=92.9):     #|
    grade = 'B'                          #|
elif(average>=73 and average<=82.9):     #|    Converts grade to Letter grade
    grade = 'C'                          #|
elif(average>=60 and average<=72.9):     #|
    grade = 'D'                          #|
elif(average<59.9):                      #|
    grade = 'F'                          #|
                                            
print('------------Results------------')               #Displays top bar
print(f'Lowest Grade  :      {min(gradelist)}')     #Displays the lowest grade in the list
print(f'modified List :      {(gradelist)}')     #Displays the highest grade in list
print(f'Scores Average:      {average:.2f}')            #Displays the value of 'Average'
print(f'Grade         :      {grade}')
print('----------------------------------------')      #Displays bottom Bar




    
            