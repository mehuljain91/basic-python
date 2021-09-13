# BMI Calculator in standard and metric measurement system

import math

print('BMI Calculator')
print('*****************************')
print('Choose measurement system: \'standard\' or \'metric\' ')
print('Type \'s\' for Standard or Type \'m\' for Metric')

sorm = input()

# try for valid input
try: 
    # if input is 's' then Standard system
    if sorm == 's':
        height_std = print('Enter height: ')
        height_feet = input('feet: ')
        height_inches = input('inches: ')
        height_std = height_feet + '.' + height_inches

        weight_std = input('Enter weight in pounds: ')
        print('height is ' + height_std + ' ft')
        print('weight is ' + weight_std + ' lb')

        height_in_inch = float(height_std) * 12
        bmi_std = (float(weight_std) / math.pow(height_in_inch, 2)) * 703
        format_bmi_std = str(bmi_std)
        print('BMI: ' + format_bmi_std[:5])
    
    # if input is 'm' then Metric system
    if sorm == 'm':
        height_mtr = input('Enter height in centimeter: ')
        height_in_m = float(height_mtr) / 100
        weight_mtr = input('Enter weight in kg: ')

        bmi_mtr = float(weight_mtr) / math.pow(height_in_m, 2)
        format_bmi_mtr = str(bmi_mtr)
        print('BMI: ' + format_bmi_mtr[:5])
    
    # any wrong input
    else:
        print('invalid input')

# exception
except:
    print('invalid input')

