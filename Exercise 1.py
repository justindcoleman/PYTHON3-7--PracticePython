correctTypesFirst = False
correctTypesSecond = False
name = raw_input('Please enter your name: ')
errorMessage = 'This is not a number!'
while correctTypesFirst == False:
    age = raw_input('Please enter your age: ')
    try:
        int(age)
        correctTypesFirst = True

    except ValueError:
        try:
            float(age)
            correctTypesFirst = True
        except ValueError:
            print errorMessage

while correctTypesSecond == False:
    currentYear = raw_input('Please enter the current year: ')
    try:
        int(currentYear)
        correctTypesSecond = True

    except ValueError:
        try:
            float(currentYear)
            correctTypesSecond = True
        except ValueError:
            print errorMessage

print "Hello " + name
print "You're currently "+ age
differenceBetween = 100 - int(age)
yearTheyTurnOneHundred = int(currentYear) + int(differenceBetween)
print "You'll turn 100 in the year: " + str(yearTheyTurnOneHundred)
raw_input('Press any key to exit')
