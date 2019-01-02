# get file location (presumable the native file navigation window can be used?)
# #try/except for bad input
# make a list of all the sub directory names (maybe a dict would be better?)
# crawl the list removing all non-alphanumeric characters (LEAVE ', &, and . in file names tho)
# rename files to the updated name (some logic for multiple files e.g. file1.txt, file2.txt)
# pull files into parent directory
# check that all files have been moved
# #output log showing any non-empty folders
# delete empty folders?

from os import path #i think this is how you use the native file navigator
from os import rename #renaming function that can probably be used
from os import listdir #everything in the directory (files and sub-directories)
from os import walk #two lists for each directory it visits - splitting into files and directories
