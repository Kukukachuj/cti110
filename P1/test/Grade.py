gradelist =[]
scoreamount = int(input('How many scores do you want?:'))
currentg = 0
while(True):
    while scoreamount > currentg:
        score = int(input(f'Enter score #{currentg+1} '))
        
        while(True):
            if score < 0 or score > 100:
                print('INVALID Score entered!!!!\nScore should be between 0 and 100')
                score = int(input(f'Enter score #{currentg+1} again:'))
            else:
                gradelist.append(score)
            break
        currentg+=1
