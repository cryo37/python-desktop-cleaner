import os
import shutil

path_for_desktop =os.path.expanduser("~/Desktop")

ListOfFilesAndFolder=os.listdir(path_for_desktop)

files_by_their_extention={}
# A dictionary to store the files path by extension for later segregation


for filename in ListOfFilesAndFolder:
    file_path = os.path.join(path_for_desktop,filename)
    # print (file_path)
    if os.path.isfile(file_path):
        file_extention=os.path.splitext(filename)[1]
        if file_extention not in files_by_their_extention:
            files_by_their_extention[file_extention]=[]

        files_by_their_extention[file_extention].append(file_path)

    for ext,list_of_files in files_by_their_extention.items():
        foldername= f"{ext[1:].upper()} Files"
        folder_path= os.path.join(path_for_desktop,foldername)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
   # Create the folder if it does not exists

    for files in list_of_files:
        shutil.move(files,folder_path)
