name = input ('What is your name?\n')
while name == (''):
    print('You did not type a name')
    name = input('What is your name?\n')
print(f'Hello {name}')
age = int(input('What is your age? \n'))
while not age > 0 and age < 200 :
    print('Thats not a valid age...')
    age = int(input('What is your age?'))
ran_num = int(input('Type a random number between 1 - 100 \n' )) 
while  ran_num < 1 or ran_num > 100 :
    print ('Not Valid must be a number 1 - 100')
    ran_num = int(input('Please input a random number 1 - 100 \n'))
print(f'Your name is {name} and your age is {age} and your random number minus 1 is {ran_num - 1}')

    
