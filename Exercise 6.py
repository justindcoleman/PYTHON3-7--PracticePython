completionState = False
userList = []
palindromeCheck = []
while completionState is not True:
    userAnswer = raw_input('Please enter a word: ')
    if userAnswer.isalpha():
        list(userAnswer)
        print 'using range:'
        print userAnswer[0:len(userAnswer)]
        print 'using only list name:'
        print userAnswer
        print 'backwards \(i think\):'
        print userAnswer[len(userAnswer):0]
        # lengthOfAnswer = len(userAnswer)
        # print('okay it\'s working so far')
        # for i in userAnswer:  # type: object
        #     print userList
        #     userList.append(int(userAnswer[i]))
    else:
        print ('Please enter a word next time!')
