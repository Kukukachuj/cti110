first_int = int(input('First Integer: '))
second_int= int(input('Second Integer: '))
if (first_int <= second_int):
    first_int = first_int
    while not( first_int > second_int) :
        print(first_int,end=" ")
        first_int = first_int + 5
else:
    print('Second integer can\'t be less than the first.')