#importing some stuffs
import os #this is import for some operating system (OS) functions

##some global variable for this module
directory = "users/"
extension = ".txt"


def choice():
    print('{:_<80}'.format(""))
    invalid = True
    while invalid:
        invalid = False
        try:
            choice = int(input("ACTION: "))
        except:
            print("-------WARNING: Invalid input-------")
            invalid = True
    return choice

def name():
    print('{:_<80}'.format(""))
    name = input("USERNAME: ").upper()
    return name

def verify(user_name):
    full_dir = directory + user_name + extension
    if os.path.isfile(full_dir):
        return True
    else:
        return False

def create(user_name):
    full_dir = directory + user_name + extension
    file = open(full_dir,"w")
    file.close()

def update(user_name,user_data):
    full_dir = directory + user_name + extension
    file = open(full_dir,"w")
    #file.write("This is line %d\r\n" % (i+1))
    for each in user_data:
        file.write(each[0]+',')
        file.write(each[1]+',')
        file.write(each[2]+'\n')
    file.close()
    

