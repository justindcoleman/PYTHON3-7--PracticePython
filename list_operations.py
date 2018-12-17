import random

while True:
    numlist = []
    listavg = 0
    count = int(input("How big is the list: "))
    while count > 0:
        randint = random.randint(10, 100)
        numlist.append(randint)
        count = count - 1

    print("The list contains: ")
    for i in numlist:
        print(i, end="\t")
    print()
    print("The first and last elements are:", numlist[0], numlist[-1])
    print("The largest value is: ", max(numlist))
    for i in numlist:
        listavg = listavg + i
    average = listavg / len(numlist)
    print("The average of the elements is: ", average)
    print("List elements in descending order are: ")
    numlist.sort(reverse = True)
    for i in numlist:
        print(i, end="\t")
    print()
    fivelist = [i + 5 for i in numlist]
    print("The contents of the list after adding 5 to each element:")
    for i in fivelist:
        print(i, end="\t")
    print()
    print("The contents of the list after adding 1, 2, and 5:")
    numlist.insert(0, 1)
    numlist.insert(3, 5)
    numlist.append(2)
    for i in numlist:
        print(i, end="\t")
    print()
    del numlist[0:4]
    numlist.pop(-1)
    print("List after removing the first 4 and last elements:")
    for i in numlist:
        print(i, end="\t")
    print()
    goAgain = input("Do is again? (yes or no): ")
    if goAgain[0] is "n":
        break