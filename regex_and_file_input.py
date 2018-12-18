import re
fileName = input("Enter a file name (including extension): ")
userRegex = input("Enter regex expression: ")
regexMatches = []
fileHandle = open(fileName, 'r')

for line in fileHandle:
    regexMatches.extend(re.findall(userRegex, line))

print("Matches:")
count = 0
for item in regexMatches:
    count += 1
    print("Item" + str(count) + ": " + item)
