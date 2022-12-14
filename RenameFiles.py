import os

def rename_folders(dirname, new_folder_name):
    folders = os.listdir(dirname)
    for i in range(len(folders)):
        os.rename(dirname + '/' + folders[i], dirname + '/' + new_folder_name + "_" + str(i))

def rename_files(dirname, folder_name, extension):
    files = os.listdir(dirname)
    for i in range(len(files)):
        os.rename(dirname + "/" + files[i], dirname + "/" + folder_name + "_" + str(i) + extension)

label_data_root = "../data/validation/label_data"
raw_data_root = "../data/validation/raw_data"

rename_folders(label_data_root, "validation_label_data")
rename_folders(raw_data_root, "validation_raw_data")

for folder in os.listdir(label_data_root):
    rename_files(label_data_root + "/" + folder, folder, ".json")
    print("Files in", folder, "renamed.")

for folder in os.listdir(raw_data_root):
    rename_files(raw_data_root + "/" + folder, folder, ".wav")
    print("Files in", folder, "renamed.")