def heading(text):
    text = text.upper()
    print("\n\n\n",'{:^80}'.format(text))

def input_warning():
    print("WARNING: INVALID INPUT")

def new_here_msg():
    print('{:_<80}'.format(""),"\n")
    print(
        '{:10}'.format("S.N."),
        '{:70}'.format("ACTION")
        )
    print(
        '{:10}'.format("1"),
        '{:70}'.format("Yes, Create an account")
        )
    print(
        '{:10}'.format("2"),
        '{:70}'.format("No, I mistyped my username")
        )


#this is a function to print the action i.e. borrow,return etc.
def menu():
    print('{:_<80}'.format(""),"\n")
    print(
        '{:10}'.format("S.N."),
        '{:70}'.format("ACTION")
        )
    print(
        '{:10}'.format("1"),
        '{:70}'.format("Borrow book")
        )
    print(
        '{:10}'.format("2"),
        '{:70}'.format("Return book")
        )
    print(
        '{:10}'.format("3"),
        '{:70}'.format("Check my log")
        )
    print(
        '{:10}'.format("4"),
        '{:70}'.format("Library rules")
        )
    print(
        '{:10}'.format("5"),
        '{:70}'.format("Quit program")
        )


def matrix(data):
    print('{:_<80}'.format(""),"\n")
    print(
        '{:10}'.format("S.N."),
        '{:25}'.format("NAME"),
        '{:25}'.format("AUTHOR"),
        '{:10}'.format("QUANTITY"),
        '{:10}'.format("PRICE")
        )

    sn = 1
    for each in data:
        #because we know there are limited cols we can do;
        print(
            '{:10}'.format(str(sn)),
            '{:25}'.format(each[0]),
            '{:25}'.format(each[1]),
            '{:10}'.format(each[2]),
            '{:10}'.format(each[3])
            )
        sn += 1 #increasing the S.N.



def user_data(data):
    print('{:_<80}'.format(""),"\n")
    print(
            '{:10}'.format("S.N."),
            '{:25}'.format("BOOK"),
            '{:25}'.format("AUTHOR"),
            '{:20}'.format("BORROWED DATE"),
            )
    
    if len(data) != 0:
        sn = 1
        for each in data:
        #because we know there are limited cols we can do;
            print(
                '{:10}'.format(str(sn)),
                '{:25}'.format(each[0]),
                '{:25}'.format(each[1]),
                '{:20}'.format(each[2]),
                )
            sn += 1 #increasing the S.N.
    else:
        print("\n\n",'{:^80}'.format("EMPTY, YOU HAVENT BORROWED ANY"),"\n")
    

def library_rule():
    print('{:_<80}'.format(""),"\n")
    print(
        '{:10}'.format("1"),
        '{:70}'.format("You must create an account to borrow our books")
        )
    print(
        '{:10}'.format("2"),
        '{:70}'.format("Fine is charged for the late return of book, $0.5/day")
        )
