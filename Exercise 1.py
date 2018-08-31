correctTypes = False
name = raw_input('Please enter your name: ')
currentYear = raw_input('Please enter the current year: ')
errorMessage = 'This is not a number!'
if correctTypes == False:
    age = raw_input('Please enter your age: ')
    try:
        int(age)
    except ValueError:
        try:
            float(age)
        except ValueError:
            print errorMessage

print "Hello " + name +"!"
print "You're currently "+ age + "."
something = 100 - age
yearTheyTurnOneHundred = age
raw_input('Press any key to exit')
