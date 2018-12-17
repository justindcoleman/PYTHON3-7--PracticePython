print('''
Programmer: Justin Coleman
Course:     COSC 146
Due Date:   11-8-2018
Lab#:       8, part 1
''')

fopen = open("romeo.txt")
wordList = []
for line in fopen:
    split = line.split()
    for i in split:
        if i not in wordList:
            wordList.append(i)
    
    
wordList.sort()
print("Distinct words in 'romeo.xt':")
count = 0
empty = ''

for i in wordList:
    if count < 5:
        empty = empty + i + '\t'
        count = count + 1
    else:
        empty = empty + '\n' + i + '\t'
        count = 1

print(empty)