'''
Project 5
Problem Statement:
Often, we have a large number of files in a directory with names that do not follow a specific pattern or are not easy to understand. 
Renaming each file manually can be time-consuming and error-prone. To solve this problem, 
we need a program that can rename a large number of files in bulk, based on a specified pattern.

Question:
Can you develop a Python program that takes a directory path and a pattern as input, 
and renames all the files in the directory that match the pattern to a new name that follows the specified pattern?
'''

import re
from pathlib import Path

def bulk_file_rename(
    directory,  #Path to the directory
    match_pattern, #Regex pattern to match filenames
    new_name_pattern,
    start_index=1,
    renameFile=True #If True, only shows what would be renamed, If False= renames file in the folder
):
    directory = Path(directory)
    #print(directory)
    #print(Path.cwd())
    if not directory.exists():
        raise FileNotFoundError("Directory does not exist")

    files = sorted(directory.iterdir())
    counter = start_index

    for file in files:
        #print(file.name)
        if file.is_file() and re.search(match_pattern, file.name):
            new_name = new_name_pattern.format(n=counter) + file.suffix
            new_path = file.with_name(new_name)
            #print(f"new_path: {new_path}")
            if renameFile:                          #TRUE: Only shows the files that will be renamed as
                print(f"[FILE RENAMED AS:] {file.name} → {new_name}")
            else:
                if new_path.exists():               #Checks if same filename already exists
                    print(f"Skipping: {new_path.name} already exists")
                else:
                    file.rename(new_path)           #Actually renames a file in folder
                    print(f"Renamed: {file.name} → {new_name}")

            counter += 1

folderName = "Project5_Files"

bulk_file_rename(
    directory=Path.joinpath(Path.cwd(),folderName),
    match_pattern=r"report_old_.*",
    new_name_pattern="report_{n:02}",
    renameFile=True #change it to False to rename the file
)