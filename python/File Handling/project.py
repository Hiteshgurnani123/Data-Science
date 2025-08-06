#CRUD -->  Create , Read , Update , Delete

# File Handling in Python

from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f'{i+1} : {items}')


def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p , 'w') as fs:
                data = input("Enter the content you want to write in the file: ")
                fs.write(data)

        else:
            print(f"File '{name}' already exists. Please choose a different name.")
            return
        
        print(f"File '{name}' created successfully with the provided content.")

    except Exception as err:
        print(f'An Error occurred: {err}')


def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p , 'r') as fs:
                data = fs.read()
                print(data)

            print('Readed Successfully')

        else:
            print('File does not exist or is not a file. Please check the name and try again.')

    except Exception as err:
        print(f'An Error occurred: {err}')


def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print('Press 1 for Changing the name of your file')
            print('Press 2 for overwriting the content of your file')
            print('Press 3 for appending the content of your file')

            res = int(input("Enter your choice: "))

            if res ==1:
                newname = input("Enter the new name of the file: ")
                newp = Path(newname)
                p.rename(newp)

            if res == 2:
                with open(p , 'w') as fs:
                    data = input("Enter the new content you want to write in the file: ")
                    fs.write(data)

            if res == 3:
                with open(p , 'a') as fs:
                    data = input("Enter the content you want to append in the file: ")
                    fs.write(' ' +data)

    except Exception as err:
        print(f'An Error occurred: {err}')


def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print('File deleted successfully.')

        else:
            print('File does not exist or is not a file. Please check the name and try again.')

    except Exception as err:
        print(f'An Error occurred: {err}')



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check ==3:
    updatefile()

if check == 4:
    deletefile()