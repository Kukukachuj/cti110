# CTI-110
# P3HW2 - Salary
# James Moore
# 2/23/23
employee_count = 0
tovertime_pay = 0
tregular_pay = 0
tgross_pay = 0


while True:
    employee = input('Enter employee\'s name or "Done" to terminate: ')

    if employee == 'Done':
        break
    
    else:
        hours_wrked = int(input(f'how many hours did {employee} work? '))
        pay_rate= float(input(f'What is {employee} pay rate? '))
    if hours_wrked > 40:
       over_time = hours_wrked - 40 
       overtime_Pay = over_time * pay_rate * 1.5
       regular_pay = (hours_wrked * pay_rate)
    else:
        regular_pay = (hours_wrked * pay_rate)
        over_time = hours_wrked - 40 
        overtime_pay = 0
    gross_pay = overtime_pay + regular_pay 
    employee_count += 1
    tovertime_pay += overtime_pay
    tregular_pay += regular_pay
    tgross_pay += gross_pay
     
    print('-'*36)                                                                                                    #|
    print('Employee name: ',employee)                                                                                  #|
    print()                                                                                                          #|
    print('Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay')                         #| Output
    print('-'*100)                                                                                                    #|
    print(f'{hours_wrked}  \t\t {pay_rate} \t\t {over_time} \t\t {overtime_pay} \t\t ${regular_pay:.2f} \t ${gross_pay}')

print()
print(f'Total number of employees entered: {employee_count}')
print(f'Total amount payed for over time: ${tovertime_pay:.2f}')
print(f'Total amount payed for regular hours: ${tregular_pay:.2f}')
print(f'Total amount payed in gross: ${tgross_pay:.2f}')