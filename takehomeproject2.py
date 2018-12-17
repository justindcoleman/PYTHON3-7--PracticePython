print('''
Programmer: Justin Coleman
Course:     COSC 146
Due Date:   12-6-2018
Lab#:       Take Home Project #2
''')

#find number of moves to balance packets
def findMoves(packets): 
    sum = 0
    for packet in packets:
        sum = sum + packet 
    if sum % len(packets) is not 0:
        return -1
  
    difference = 0
    balance = sum / len(packets) 
    for packet in packets:
        difference = difference + abs(packet - balance) 
    return int(difference / 2) 
#

#get file and create handle
filename = input("Enter the name of the file you would like to open, including extension (.txt, .doc, etc): ")
fopen = open(filename, 'r')
#
packetCount = -1
packets = []
end = False
while end is False:
  inputs = fopen.readline().rsplit() #pull in the number of packets
  inputs = list(map(int, inputs)) #convert elements to int
  for input in inputs:
    if len(packets) < packetCount:  #fills up the list
      packets.append(input)
    else:
      if packetCount is not -1: #runs the main logic
        print(findMoves(packets))
        packets = []
      if input is -1: #final pass
        end = True
        break
      else:
        packetCount = input #for determining length of the set (list)