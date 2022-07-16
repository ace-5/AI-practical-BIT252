# WAP to input the percentage and display the division
# >=80 →  Distinction
# >=65 →  First Division
# >=55 →  Second Division
# >=40 →  Third Division
# <40  →  Fail

percentage = float(input('Enter percentage: '))
if percentage in range(0, 101):
    if percentage >= 80 : print('Distinction')
    elif percentage >= 65: print('First Division')
    elif percentage >= 55: print('Second Division')
    elif percentage >= 40: print('Third Division')
    elif percentage < 40: print('Fail')
else: print('Invalid percentage. Percentage must be in range(0, 100)')
