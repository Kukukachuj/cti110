# CTI-110
# P4HW2 - Salary
# James Moore
# 4/18/23

total_employees = 0
total_overtime = 0        # Total Variables
total_hours = 0
total_gross = 0

while True:  # Start of loop
    # Gets Employee Name
    employee = input('Enter employee\'s name or \"Done\" to terminate: ')
    if employee == 'Done':                                                  # Ends loop
        break
    else:
        hoursworked = float(
            input(f'How many hours did {employee} work: '))   # Gets Hours
        # Gets Payrate
        payrate = float(input(f'What is {employee}\'s pay rate? '))
        # Adds Employee to Total Variables
        total_employees += 1
    if hoursworked > 40:
        regpay = hoursworked * payrate
        overtime = hoursworked - 40
        # Overtime Calculations
        overtimerate = (payrate / 2) + payrate
        overtimepay = overtime * overtimerate
        # Adds To Total Variable
        total_overtime += overtimepay

    else:
        overtime = 0
        overtimepay = 0
    regpay = (hoursworked - overtime) * payrate
    grosspay = regpay + overtimepay
    # Hours and Pay Calculations
    total_hours += regpay
    total_gross += grosspay
    print('-'*36)
    print('Employee name: ', employee)
    print()
    # Prints Informations about hours, pay, overtime ect
    print('Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay')
    print('-'*100)
    print(f'{hoursworked}  \t\t {payrate:.2f} \t\t {overtime} \t\t {overtimepay:.2f} \t\t ${regpay:.2f} \t ${grosspay:.2f}')

print(f'Total number of employees entered: {total_employees}')
# Displays Total Variables,
print(f'Total amount paid for overtime: ${total_overtime}')
print(f'Total amoiunt paid for regular hours: ${total_hours:.2f}')
print(f'Total amount paid in gross: ${total_gross}')
