import os

path = full_path_of_files_whose_names_to_change = "some/path"

def change_file_names(path, suffix="IMG"):
    
    # get file names
    file_names = [file for file in os.listdir(path)]

    for count, file_name in enumerate(file_names):
        #print(file_name)
        try:
            os.rename(f'{path}/{file_name}',            #old file name
                      f'{path}/{suffix}_{count}.JPG' ), #new file name
                                                        #always provide the extension
        except:
            print("FileNotFound")
    return os.listdir(path)