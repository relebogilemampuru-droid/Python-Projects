
while True:
    operator = input('Enter an operator (+ - * /): ')
    if operator in ['+', '-', '*', '/']:
        break
    print(f'{operator} is not valid. Please try again')

while True:
    try:
        num1 = float(input('Enter the first number: '))
        break
    except ValueError:
        print('Thats not a valid number. Please numbers only')

while True:
    try:
        num2 = float(input('Enter the second number: '))
        break
    except ValueError:
        print('Thats not a valid number. Please input numbers only')

if operator == '+':
    result = num1 + num2
elif operator =='-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 ==0:
        print('Error: Cannot divide by zero')
    else:
        result = num1 / num2
        print(f'Result: {round(result, 2)}')   



