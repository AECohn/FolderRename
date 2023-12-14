import os
root_path = ""


def build_rename_list(folder_path, folder_names):
    global root_path
    folders_to_change = []
    root_path = folder_path
    for root, directories, files in os.walk(folder_path):
        for directory in directories:
            if directory in folder_names:
                old_path = os.path.join(root, directory)
                parent_name = os.path.basename(root)
                new_path = os.path.join(root, f"{parent_name}.{directory}")
                folders_to_change.append((old_path, new_path))
    return folders_to_change


# User Stuff
start_dir = input("what directory should we use?")
folder_names_to_change = input("Which folder names should we look for? Please separate them with a comma, then press enter").split(",")
temp_list = build_rename_list(start_dir, folder_names_to_change)
while True:
    for index, folder in enumerate(temp_list):
        print(f"{str(index + 1)} {folder[0]} will be renamed to {folder[1]}")
    response = input("to remove an index, enter the number of the index to remove, otherwise press 'y' to rename")
    if response != 'y':
        if response.isalnum():
            temp_list.remove(temp_list[int(response) - 1])
    else:
        with open(root_path + r"\renamelog.txt", "w") as file:  # 'w' is the write mode
            counter = 0
            for value in temp_list:
                file.write(f"{value[0]} was renamed to {value[1]}\n")
                os.rename(value[0], value[1])
                counter += 1
            print(f"{counter} folders were renamed")
        break
