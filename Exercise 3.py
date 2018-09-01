myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
isInt = False
while isInt is False:
    userNumber = raw_input('Please enter a number: ')
    try:
        int(userNumber)
        isInt = True

    except ValueError:
        try:
            float(userNumber)
            isInt = True
        except ValueError:
            print('Give me a N U M B E R')
for i in myList:
    if i < int(userNumber):
        newList.append(i)
print newList
