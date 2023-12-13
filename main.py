import os

folderNamesToChange = ["Control", "GUI", "UI", "control", "gui", "ui"]
renameLog = []
counter = 0

def rename_control_folder(folderPath):
  for root, directories, files in os.walk(folderPath):
    for directory in directories:
      if directory in folderNamesToChange:
        old_directory = directory
        old_path = os.path.join(root, directory)
        parent_name = os.path.basename(root)
        new_path = os.path.join(root, f"{parent_name}.{old_directory}")
        os.rename(old_path, new_path)
        LogStuff(old_path, new_path, folderPath)


  print(f'{counter} folders renamed')

def LogStuff(old, new, path):
  global counter
  logMessage = ""
  counter += 1
  logMessage = f"Renamed folder '{old}' to '{new}'"
  print(logMessage)
  print(path + "\log.txt")
  renameLog.append(f"{counter}: {logMessage}")
  WriteLog(renameLog, path + r"\renamelog.txt")

def WriteLog(list, fileName):
  with open(fileName, "w") as file: #'w' is the write mode
    for logValue in list:
      file.write(f"{logValue}\n")

startDir = input("what directory should we use?")
rename_control_folder(startDir)