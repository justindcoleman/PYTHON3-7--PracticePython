isInt = False
errorMessage = 'This is not a number!'
while isInt is False:
    userAnswer = raw_input('Please enter a number: ')
    try:
        int(userAnswer)
        isInt = True

    except ValueError:
        try:
            float(userAnswer)
            isInt = True
        except ValueError:
            print errorMessage

divideAnswer = int(userAnswer) % 2

if int(userAnswer) % 4 is 0:
    print('Your number is a multiple of four!')
elif divideAnswer is 0:
    print ('Your number is even!')
elif divideAnswer is not 0:
    print ('your number is odd!')
else:
    print('How did you get this error?\n\n \(odd or even determination\)')
