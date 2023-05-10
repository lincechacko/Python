import os.path
import struct
def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference


def foo():
    print("New dive introduced")


def ham():
    print("Drive disconnected")


dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives1 = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(drives1)
length=len(drives1)
while True:
    drives2 = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    print(drives2)
    lenght2=len(drives2)
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(drives2, drives1)
    path=x
    in_filename='/testing.txt'
    if x:
        print("New drives:     " + str(x))
        try:
           file = open(os.path.join(path[0], in_filename), "r")
           print("File open successful")
           print("Output of Read function is ")
           file_size = os.path.getsize('D:\\ROOTFILE.txt')
           print("File Size is :", file_size, "bytes")
           for line in file:
               x=0
               y=0
               for word in line.split():
                   print(word)
           break      
        except FileNotFoundError:
            print("File not found")   
   
        foo()
    x = diff(drives2, drives1)
    if x:
        print("Removed drives: " + str(x))
        ham()
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
