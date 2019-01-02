# get file location (presumable the native file navigation window can be used?)
# #try/except for bad input
# make a list of all the sub directory names (maybe a dict would be better?)
# crawl the list removing all non-alphanumeric characters (LEAVE ', &, and . in file names tho)
# rename files to the updated name (some logic for multiple files e.g. file1.txt, file2.txt)
# pull files into parent directory
# check that all files have been moved
# #output log showing any non-empty folders
# delete empty folders?

import os.path #i think this is how you use the native file navigator
import os.rename #renaming function that can probably be used

