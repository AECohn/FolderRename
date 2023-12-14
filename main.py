import os

folderNamesToChange = []
renameLog = []
counter = 0


# To-Do: Program should initially build a list of all folders that will be renamed,
# the user can then enter an index id to remove that index from the list, and then after confirming, the remaining folders in the list will be renamed
def renamecontrolfolder(folderpath, foldernames):
    for root, directories, files in os.walk(folderpath):
        for directory in directories:
            if directory in foldernames:
                old_directory = directory
                old_path = os.path.join(root, directory)
                parent_name = os.path.basename(root)
                new_path = os.path.join(root, f"{parent_name}.{old_directory}")
                os.rename(old_path, new_path)
                logstuff(old_path, new_path, folderpath)
    print(f'{counter} folders renamed')


def logstuff(old, new, path):
    global counter
    counter += 1
    logmessage = f"Renamed folder '{old}' to '{new}'"
    print(logmessage)
    print(path + "\log.txt")
    renameLog.append(f"{counter}: {logmessage}")
    writelog(renameLog, path + r"\renamelog.txt")


def writelog(folderlist, filename):
    with open(filename, "w") as file:  # 'w' is the write mode
        for logValue in folderlist:
            file.write(f"{logValue}\n")


startDir = input("what directory should we use?")
renamecontrolfolder(startDir, folderNamesToChange)
