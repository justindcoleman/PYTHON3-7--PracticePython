correctTypes = False
#correctTypesSecond = False
name = raw_input('Please enter your name: ')
errorMessage = 'This is not a number!'
while correctTypes is False:
    age = raw_input('Please enter your age: ')
    try:
        int(age)
        correctTypes = True

    except ValueError:
        try:
            float(age)
            correctTypes = True
        except ValueError:
            print errorMessage

correctTypes = False
while correctTypes is False:
    currentYear = raw_input('Please enter the current year: ')
    try:
        int(currentYear)
        correctTypes = True

    except ValueError:
        try:
            float(currentYear)
            correctTypes = True
        except ValueError:
            print errorMessage

correctTypes = False
while correctTypes is False:
    printIterations = raw_input('Enter a number: ')
    try:
        int(printIterations)
        correctTypes = True

    except ValueError:
        try:
            float(printIterations)
            correctTypes = True
        except ValueError:
            print errorMessage

print "Hello " + name
print "You're currently " + age
differenceBetween = 100 - int(age)
yearTheyTurnOneHundred = int(currentYear) + int(differenceBetween)
print "You'll turn 100 in the year: " + str(yearTheyTurnOneHundred)
raw_input('Press any key to exit')
