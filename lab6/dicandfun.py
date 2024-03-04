#ex3
import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None

path = "/User/qwerty/Desktop/file.txt"

exists, filename, directory = path_info(path)

if exists:
    print(f"Path exists")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print(f"Path does not exist")

#ex4
with open('text.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
    print(count)
    
#ex5
list = [1, 2, 3, 4, 5]
with open('text.txt', 'w') as f:
    for i in list:
        f.write(str(i) + ' ')

#ex6
import string

def generate():
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as f:
            pass

generate()

#ex7
with open('text.txt', 'r') as rf:
    with open('text-copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

#ex8
import os
path = "/User/qwerty/Desktop/file.txt"

if os.path.exists(path):
  os.remove(path)
else:
  print("The file does not exist")
    
#ex1
import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_directories_and_files(path):
    directories = []
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        elif os.path.isfile(item_path):
            files.append(item)
    return directories, files

path = "/User/qwerty/Desktop/file.txt"

print("Directories:")
print(list_directories(path))

print("\nFiles:")
print(list_files(path))

print("\nDirectories and Files:")
directories, files = list_directories_and_files(path)
print("Directories:")
print(directories)
print("Files:")
print(files)

#ex2
import os

def check_access(path):
    access_info = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return access_info

path = "/User/qwerty/Desktop/file.txt"

access_info = check_access(path)

print(f"Path: {path}")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")

