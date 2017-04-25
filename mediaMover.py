import os
import shutil
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
foldersToDeleteArray = []
# ask for the directory the user wants to use
location = askdirectory()


with open("extensionsToMove.txt") as f:
    extensionsToMove = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end
# of each line
extensionsToMove = [x.strip() for x in extensionsToMove]

extensionListSize = len(extensionsToMove)


for path, subdirs, files in os.walk(location):
    for filename in sorted(files):
        f = os.path.join(path, filename)
        # searching for files ending with this extensions
        for num in range(0, extensionListSize):
            if filename.endswith(extensionsToMove[num]):
                SearchResultFileName = (os.path.split(f)[1])
                # print "this is searchResult " + str(SearchResultFileName)
                twoFoldersUp = os.path.normpath(os.path.join(f, '../../'))

                oneFolderUp = os.path.normpath(os.path.join(f, '../'))
                if(oneFolderUp not in foldersToDeleteArray):
                    foldersToDeleteArray.append(oneFolderUp)

                shutil.move(f, twoFoldersUp)

for item in foldersToDeleteArray:
    shutil.rmtree(item)
