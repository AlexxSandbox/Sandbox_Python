# open files and create new
def rw():
    with open('dataset_24465_4.txt') as f, open('test.txt', 'w') as n:
        text = f.readlines()
        n.writelines(text[::-1])


# os
import os.path

print(os.listdir())  # show dirs and files in current dir
print(os.listdir('c:/Windows'))
print(os.getcwd())  # show path to current dir
print(os.path.exists('datetime.py'))  # True
print(os.path.exists('new.py'))  # False
print(os.path.abspath('datetime.py'))  # C:\Dev\Sandbox_Python\Python basics\datetime.py


# show dirs and files in current dir
def print_path():
    """ print all path, dirs and files in dirs """
    for current_dir, dirs, files in os.walk('.'):
        print(current_dir, dirs, files)


def find(root='.', type_file='.py'):
    """ Find all path where is some files """
    tmp = []
    for path, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(type_file):
                tmp.append(path[2:].replace('\\', '/'))
                break
    return tmp


# lib for copy
import shutil

shutil.copytree('test', 'test/test') # copy test inside test
