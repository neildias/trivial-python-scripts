import os
import re
import win32api

def find_file(root_folder, rex): #rex inside
    for root,dirs,files in os.walk(root_folder):
        print(root, dirs, files)
        for f in files:
            #result = rex.search(f)
            #if result:
            if
                print(f'found here {os.path.join(root, f)}')
    else:
        print("Found None!")


def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )

print("What do you want to search? Enter here ", end=" ")

search_this = input()
search_drive = input("Do you wish to search in a specific location? press y for yes, any-key for an exhaustive search")
if search_drive == "y":
    search_drive = input("Please provide the file path to search in here:: ")
    rex = re.compile(search_this)
    find_file(search_drive, rex)
else:
    find_file_in_all_drives( search_this )
