userAnswer = int(input("Give me a number: "))

listRange = list(range(1, userAnswer+1))

divisorList = []

for i in listRange:
    if userAnswer % i is 0:
        divisorList.append(i)

print(divisorList)
