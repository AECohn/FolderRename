import os

foldernamestochange = ["test", "ui"]


# To-Do: Program should initially build a list of all folders that will be renamed,
# the user can then enter an index id to remove that index from the list, and then after confirming, the remaining folders in the list will be renamed
def buildrenamelist(folderpath, foldernames):
    folder_names = []
    counter = 0
    for root, directories, files in os.walk(folderpath):
        for directory in directories:
            if directory in foldernames:
                old_path = directory
                oldpath = os.path.join(root, directory)
                parentname = os.path.basename(root)
                new_path = os.path.join(root, f"{parentname}.{old_path}")
                counter += 1
                #logmessage = f"'{old_path}' will be changed to '{new_path}'"
                folder_names.append((old_path, new_path))
    return folder_names


'''def buildList(old, new, path):
    global counter
    
    writelog(renamelist, path + r"\renamelog.txt")'''


def writelog(folderlist, filename):
    with open(filename, "w") as file:  # 'w' is the write mode
        for logValue in folderlist:
            file.write(f"{logValue}\n")

startDir = input("what directory should we use?")
templist = buildrenamelist(startDir, foldernamestochange)
while True:
    for index, folder in enumerate(templist):
        print(f"{index+1} {folder[0]} will be renamed to {folder[1]}")
    response = input("to remove an index, enter the number of the index to remove, otherwise press 'y' to rename")
    if response != 'y':
        if response.isalnum():
            templist.remove(templist[int(response)-1])
    #else:
        #for folder in templist:
        ##os.rename(oldpath, newpath)

#def renamefolders(folderlist):
    #for folder in folderlist:
