# PracticePython
working through the exercises on http://www.practicepython.org/exercises/

# Python for Everybody exercises on https://www.py4e.com/
   1. file_operations_advanced_challenge instructions:
    Jennifer is a teacher in the first year of a primary school. She has gone for a trip with her class today. She has taken a packet of candies for each child. Unfortunately, the sizes of the packets are not the same.  Jennifer is afraid that each child will want to have the biggest packet of candies and this will lead to quarrels or even fights among children. She wants to avoid this. Therefore, she has decided to open all the packets, count the candies in each packet and move some candies from bigger packets to smaller ones so that each packet will contain the same number of candies. The question is how many candies she has to move.  The input file consists of several blocks of data. Each block starts with the number of candy packets N followed by N integers giving the number of candies in each packet. After the last block of data there is the number -1.  The output should contain one line with the smallest number of moves for each block of data. One move consists of taking one candy from a packet and putting it into another one. If it is not possible to have the same number of candies in each packet, output the number -1.
        SAMPLE INPUT FILE (1.txt)
        5
        1 1 1 1 6
        2
        3 4
        -1
        SAMPLE SCREEN OUTPUT
        4
        -1
    I tried to make it cover a lot of corner cases (i.e. what if all of the input is on one line or broken up by mulitple lines)
    
    2. file_operations_1:
        open a file for output, write some random numbers to it.  reopen the file for input, read the contents, display them in a particular way, do some math on them.  open the file back up in append mode, and add that math in there.

    3. file_operations_2:
        more file operation practice.  Script reads from a file (romeo.txt) and outputs the distinct words in alphabetical order.  No regex allowed.
    4. list_operations:
        The script creates a list and fills it with a user defined amount of random numbers (range 10-100) and does various operations to them.
    5. file_operations_and_dicts.py:
        reads emails information from a text file (see included mbox-short.txt), imports relevent information into a dict, gets counts and times, outputs that info to console.  no regex allowed
