## pathlib might be a better choice than using os.walk, etc

# get file location (presumable the native file navigation window can be used?) **
# make a list of all the sub directory names (maybe a dict would be better?) **
# crawl the list removing all non-alphanumeric characters (LEAVE ', &, and . in file names tho) **
# rename files to the updated name (some logic for multiple files e.g. file1.txt, file2.txt)
# pull files into parent directory
# check that all files have been moved
# #output log showing any non-empty folders
# delete empty folders?

import re
import itertools
from os import walk, path, replace
from tkinter.filedialog import askdirectory


#
rootList = []
directoryList = []
filesList = []
directoriesToWorkOn = askdirectory()
for root, directory, files in walk(directoriesToWorkOn):
    if root not in rootList:
        rootList.extend(root)
    if directory not in directoryList:
        directoryList.extend(directory)
    if files not in filesList:
        # print("FILES:  ", type(files), files, "\n")
        filesList.extend(files)
#

#
sanitizedFilesList = []
for files in filesList:
    cleanedName = re.sub("[^a-zA-Z0-9.'& ]", '', files)
    sanitizedFilesList.append(cleanedName)
#
#
rootLocation = ''.join(rootList[0:3])

for file, sanitizedFile in zip(filesList, sanitizedFilesList):
    print(file, sanitizedFile)

#

# for files in filesList:
#     print(path.abspath)
# for entry in filesList:
#     print("filesList: ", entry)
# for entry in sanitizedFilesList:
#     print("sanitizedFilesList: ", entry)
# for entry in sanitizedFilesList:
#     print(entry)
