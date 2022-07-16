# WAP to calculate the factorial of an input number
def factorial(num):
    return 1 if (num==1 or num==0) else num * factorial(num - 1)

num = int(input('Enter a number: '))
print(f'Factorial of {num} is {factorial(num)}')