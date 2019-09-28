print('Please Choose Two Numbers')

number_one = int(input('Input First Number: '))
number_two = int(input('Input Second Number: '))

print('Please Choose The Arithmetic Operation - "+", "-", "*", "/"')
operator = input('Input Arithmetic Operation: ')

if operator == '+':
    print(number_one + number_two)
elif operator == '-':
    print(number_one - number_two)
elif operator == '*':
    print(number_one * number_two)
elif operator == '/':
    if number_two == 0:
        print('Termination - Division by Zero - No Result')
    else:
        print(number_one / number_two)
else:
    print('Wrong Input')
