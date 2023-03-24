# CTI-110
# P3HW2 - Salary
# James Moore
# 2/23/23

e_name = input("Enter employee's name: ")                      #|
hours_wrked= float(input('Enter number of hours worked: '))     #| To read data from user
pay_rate= float(input('Enter employee\'s pay rate: '))          #| 


overTime_pay = 0.0                                #|
over_time = 0.0                                   #|
if hours_wrked > 40:                              #|
	over_time = hours_wrked - 40                  #| To calculate total pay overtime and regular pay   
	overt_payRate = pay_rate + (pay_rate * 0.5)   #| 
	overTime_pay = over_time * overt_payRate      #|
	regular_pay = 40 * pay_rate                   #|
else:
	regular_pay = hours_wrked * pay_rate


gross_pay = regular_pay + overTime_pay                #|To calculate gross pay


print('-'*36)                                                                                                    #|
print('Employee name: ',e_name)                                                                                  #|
print()                                                                                                          #|
print('Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay')                         #| Output
print('-'*100)                                                                                                    #|
print(f'{hours_wrked}  \t\t {pay_rate} \t\t {over_time} \t\t {overTime_pay} \t ${regular_pay:.2f} \t ${gross_pay}')