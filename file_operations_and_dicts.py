##actually testing ssh set up
#
while True:
    filename = input('Enter a file name: ') #get file name
    
    #open file for reading & create a list with the From details
    document = []
    try:
        with open(filename, 'r') as fopen:
            for line in fopen:
                if 'From' in line and 'From:'  not in line:
                    document.append(line.strip())
        break
    except FileNotFoundError:
        print("{entered} not found, please try again.".format(entered = filename))
    #

#remove duplicates in the list
document = list(set(document))
#

#pull out just the hours and put them in a list
emailList = []
for i in document:
    colon = i.find(":")
    hours = i[(colon-2):colon]
    emailList.append(hours)
emailList.sort()
#

#create a dictionary with emailList elements as keys
emailDict = {key: 0 for key in emailList}
#

#create counts as values in the dict
for i in emailList:
    if i in emailDict:
        emailDict[i] = emailDict[i] + 1
#

#turn into a list of tuples
tuplesList = list(emailDict.items())
#

#formatting the output
for i in tuplesList:
    for y in i:
            print(y, sep="\n", end=" ")
    print()
#