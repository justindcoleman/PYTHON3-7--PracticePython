import re
#
while True:
    fileName = input("Enter a file name (including extension): ")
    try:
        fileHandle = open(fileName, 'r')
        break
    except FileNotFoundError:
        (print("{entered} not found, please try again.".format(entered=fileName)))
#
#
userRegex = input("Enter regex expression: ")
while not userRegex:
        userRegex = input("Please try again.  Enter regex expression: ")
#

#
regexMatches = []
for line in fileHandle:
    regexMatches.extend(re.findall(userRegex, line))

#

#
print("Matches:")
count = 0
for item in regexMatches:
    count += 1
    print("Found Item " + str(count) + ": " + item)
#