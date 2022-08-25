import os


# always copy this file in the folder in which 
# the files to rename are

pwd = os.getcwd()
print(pwd)

for old_name in os.listdir():
    if ".py" in old_name:
        continue
    # print(file.split()[:])
    
    new_name = " ".join(old_name.split()[1:])
    os.rename(old_name, new_name)
    