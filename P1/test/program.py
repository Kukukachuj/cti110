# set global variables
numOfEmp = 0               # holds total employees entered
totalOverTimePay = 0       # holds total over time pay for all employees
totalRegPay = 0            # holds total regular pay for all employees
totalGrossPay = 0          # holds total gross pay for all employees

# now, run a loop until user wishes to exit
while True:
    
    # in each iteration, enter employee's name, hours worked, and pay rate
    employee = input("Enter employee's name or \"None\" to terminate: ")
    
    # check if name is "None", then break the loop without any further user input
    if employee == "None":
        break
    else:
        
        # if correct name then increase employee count by 1
        numOfEmp += 1
    
    hours_wrked = float(input("How many hours did " + employee + " worked? "))
    pay_rate = float(input("What is " + employee + "\' pay rate? "))
    
    # now, for this employee, set variables to calculate values
    over_time = 0
    overtime_Pay = 0
    regular_Pay = 0
    gross_pay = 0
    
   
    if hours_wrked > 40:
        
       
        over_time = hours_wrked - 40
        
        overtime_Pay = over_time * pay_rate * 1.5
        
        
        regular_pay = 40*pay_rate
        
      
        gross_Pay = regular_pay + overtime_Pay
    else:
        
        
        regular_pay = hours_wrked*pay_rate
        gross_pay = regular_pay
    
    
    totalOverTimePay += overtime_Pay
    
    
    totalRegPay += regular_pay
    
    
    totalGrossPay += gross_pay
    
    
    print("\nEmployee name: " + employee + "\n")
    
    print('-'*36)                                                                                                    #|
    print('Employee name: ',employee)                                                                                  #|
    print()                                                                                                          #|
    print('Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay')                         #| Output
    print('-'*100)                                                                                                    #|
    print(f'{hours_wrked}  \t\t {pay_rate} \t\t {over_time} \t\t {overtime_pay} \t\t ${regular_pay:.2f} \t ${gross_pay}')

# once the loop terminates, print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print("Total number of employees entered:", numOfEmp)
print("Total amount payed for over time: $" + ':.2f'.format(totalOverTimePay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(totalRegPay))
print("Total amount payed in gross: $" + '{:.2f}'.format(totalGrossPay))