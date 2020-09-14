directory = "logs/"
extension = ".txt"

def create(user_name):
    full_dir = directory+user_name+extension
    file = open(full_dir,"w")
    file.close()

def update(user_name,log_msg):
    full_dir = directory + user_name + extension
    file = open(full_dir,"a")
    file.write(log_msg)
    file.write('\n')
    file.close()

def read(user_name):
    full_dir = directory+user_name+extension
    file = open(full_dir,"r")
    contents =file.read()
    
    print('{:_<80}'.format(""),"\n")
    print(contents)
    file.close()
    
