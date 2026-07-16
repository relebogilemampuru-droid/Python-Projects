try:
    weight = float(input('Enter your weight: '))
    unit = input('Kilograms or Pounds? (K or L): ').upper()

    if unit == 'K':
        weight = weight * 2.205
        unit = 'lbs'
        print(f'Your weight is: {round(weight, 1)} {unit}')      

    elif unit == 'L':
        weight = weight / 2.205
        unit = 'kgs'
        print(f'Your weight is: {round(weight, 1)} {unit}')      

    else: 
        print(f'{unit} was not valid')

except ValueError:
    print('Please enter numbers only')

