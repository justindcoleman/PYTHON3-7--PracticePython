# get file location (presumable the native file navigation window can be used?) **
# #try/except for bad input
# make a list of all the sub directory names (maybe a dict would be better?) **
# crawl the list removing all non-alphanumeric characters (LEAVE ', &, and . in file names tho)
# rename files to the updated name (some logic for multiple files e.g. file1.txt, file2.txt)
# pull files into parent directory
# check that all files have been moved
# #output log showing any non-empty folders
# delete empty folders?

from os import walk  # everything in the directory (files and sub-directories)
from tkinter.filedialog import askdirectory
import re

rootList = []
directoryList = []
filesList = []

directoriesToWorkOn = askdirectory()
# directoriesToWorkOn = input("Please enter a directory: ")

# for root, dirs, files in walk(directoriesToWorkOn):
#     print("root: ", root)
#     print("directories: ", dirs)
#     print("files: ", files)

for root, directory, files in walk(directoriesToWorkOn):
    if root not in rootList:
        rootList.extend(root)
    if directory not in directoryList:
        directoryList.extend(directory)
    if files not in filesList:
        # print("FILES:  ", type(files), files, "\n")
        filesList.extend(files)





rootLocation = ''.join(rootList[0:3])
# for entry in filesList:
#     print(type(entry), entry, sep="\t")
# print()
# print()


print(rootLocation + directoryList[1])
