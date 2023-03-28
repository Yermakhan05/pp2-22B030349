import os


def createFile(fname):
    f = open("{}.txt".format(fname), "x")
def readFile(fname):
    f = open("{}.txt".format(fname), "r")
    print(f.read())

def appendFile(fname):
    text = str(input())
    f = open("{}.txt".format(fname), "a")
    f.write("\n{}".format(text))
    f.close()
    f = open("{}.txt".format(fname), "r")
    print(f.read()+"\n")
    print("Add the text above {}.txt:".format(fname))
    print("The Last Of Us!")

def overwriteFile(fname):
    text = str(input())
    f = open("{}.txt".format(fname), "w")
    f.write("{}".format(text))
    f.close()

def removeFile(fname):
    if os.path.exists("{}.txt".format(fname)):
     os.remove("{}.txt".format(fname))
    else:
     print("The file does not exist")

print("*******************")
print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically): ').strip()

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')