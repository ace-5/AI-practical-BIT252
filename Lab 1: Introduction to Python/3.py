# WAP to calculate sum, diff, product and quotient between two input numbers using a single function

def calculate(x, y, sum=False, diff=False, product=False, quotient=False):
    """
    Pass two numbers and required calculation's name with value True to obtain result\n
    Eg: calculate(x, y, sum=True) -> prints sum of x and y  
    """
    if sum: print(x+y)
    if diff: print(x-y)
    if product: print(x*y)
    if quotient: print((x/y))\

x = float(input('Enter first number: '))
y = float(input('Enter second number: '))


# performing sum, difference, quotient for demonstration
calculate(x, y, sum = True, diff=True, quotient=True)