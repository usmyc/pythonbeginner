from tkinter import E


num1 = float(input('Enter first number:'))
op = input('Enter operation:')
num2= float(input('Enter second number:'))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1-num2)
elif op ==  '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:
    print('Invalid operation.')