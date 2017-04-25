import os
import shutil
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()
# show an "Open" dialog box and return the path to the selected file

# array to hold folder names to delete
foldersToDeleteArray = []

# ask for the directory the user wants to use
location = askdirectory()

# read extension names from text file
with open("extensionsToMove.txt") as f:
    extensionsToMove = f.readlines()

# removes whitespace from each line
extensionsToMove = [lines.strip() for lines in extensionsToMove]

# size of extension array
extensionListSize = len(extensionsToMove)


for path, subdirs, files in os.walk(location):
    for filename in sorted(files):
        f = os.path.join(path, filename)

        # loop through each extension from extensionsToMove array
        for num in range(0, extensionListSize):

            if filename.endswith(extensionsToMove[num]):

                # folder two directories up, moving file here
                twoFoldersUp = os.path.normpath(os.path.join(f, '../../'))

                # folder file is currently in
                oneFolderUp = os.path.normpath(os.path.join(f, '../'))

                # create array of folders to delete
                if(oneFolderUp not in foldersToDeleteArray):
                    foldersToDeleteArray.append(oneFolderUp)

                # move file (f) to the directory twoFoldersUp
                shutil.move(f, twoFoldersUp)

# delete all folders in foldersToDeleteArray
for item in foldersToDeleteArray:
    shutil.rmtree(item)
