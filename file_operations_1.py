import random

loop = 0
fname = input("Enter a file name: ")
fout = open(fname, 'w+')		
while loop is not 10:
	rando = random.randint(10, 20)
	fout.write(str(rando))
	fout.write("\n")
	loop = loop + 1
fout.close()

fout2 = open(fname, 'r+')
total = 0
count = 0
print("Contents of the input file \'", fname, "\':", sep="")
for line in fout2:
	print(line.rstrip())
	total = total + int(line)
	if int(line) > 15:
		count = count + 1

total = total /10
total =  '%.1f' % total
count = str(count)
avgtext = "Average of the numbers in the file: " + str(total)
counttext = "Count of the numbers > 15: " + str(count)
print(avgtext)
print(counttext)
fout2.close()

fout3 = open(fname, "a")
fout3.write("\n")
fout3.write(avgtext)
##fout3.write(total)
fout3.write("\n")
fout3.write(counttext)
##fout3.write(count)
fout3.close()
