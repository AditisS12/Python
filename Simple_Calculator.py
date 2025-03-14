print('Enter two number')
a=float(input('First number: '))
b=float(input('Second number: '))
print('Select an operation to perform (+,-,/,*)')
i=input('+,-,/,*')
if i=='+':
    print(f'Addition = {a+b}')
elif i=='-':
    print(f'Subtraction = {a-b}')
elif i=='/':
    print(f'Division = {a/b}')
elif i=='*':
    print(f'Multiplication = {a*b}')
else:
    print('Invalid Operator')
