import os

folderNamesToChange = ["Control", "GUI", "UI"]


def rename_control_folder(folderPath):
  logMessage = ""
  counter = 0
  renameLog = []
  for root, directories, files in os.walk(folderPath):
    for directory in directories:
      if directory in folderNamesToChange:
        old_directory = directory
        print(old_directory)
        old_path = os.path.join(root, directory)
        parent_name = os.path.basename(root)
        new_path = os.path.join(root, f"{parent_name}.{old_directory}")
        os.rename(old_path, new_path)
        counter += 1
        logMessage = f"Renamed folder '{old_path}' to '{new_path}'"
        print(logMessage)
        print(folderPath+"\log.txt")
        renameLog.append(f"{counter}: {logMessage}")
        WriteLog(renameLog, folderPath+"\renamelog.txt")

  print(f'{counter} folders renamed')


def WriteLog(list, fileName):
  with open(fileName, "w") as file: #'w' is the write mode
    for logValue in list:
      file.write(f"{logValue}\n")

# Specify the starting directory
start_dir = "C:\Workbench\_temp"


# Start the process
rename_control_folder(start_dir)