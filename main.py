##-------------------------PROGRAM RUNS FROM HERE--------------------------##


##--------------------------IMPORTING FUNCTIONS----------------------------##
import matrix
import user
import log
import display
import book

#creating 2d list of books at the start of the program
book_list = matrix.create("books_in_self.txt")

#showing welcome msg
display.heading("welcome to library")

##------------------------USER VERIFICATION PART---------------------------##

verified = False #first verified is false
while not verified: # we loop until a user is verified
    #asking user for username
    user_name = user.name() #returns input taken
    
    #checking the newness of user
    verified = user.verify(user_name) #returns 'T' or 'F' by checking data

    if verified:#if verified we break the loop instantly
        verified = True
    else:#if still not verified we try to verify
        display.heading("new here?")
        display.new_here_msg(); #display some msg
        while True: #force user to login or signup
            user_choice = user.choice();
            if user_choice == 1:
                #account creating code goes here
                user.create(user_name)
                log.create(user_name)
                print("ACCOUNT CREATION : SUCCESSFUL")
                verified = True
                break #we break our loop
            elif user_choice == 2:
                break #we break our program to change username
            else:
                display.input_warning()
        

    


##---------------------------AFTER LOGGED PART-----------------------------##

print("LOGGED AS "+user_name)
user_data = matrix.create("users/"+user_name+".txt")
#print(user_data)
run = True
while run: #run program until user wants to quit
    display.heading("menu")
    display.menu()

    #perform action according to user choice
    invalid = True
    while invalid: #take input until it is valid
        invalid = False
        user_choice = user.choice();
            
        if user_choice == 1: #if user select to borrow
            display.heading("which book are you borrowing?")
            display.matrix(book_list)
            user_select = user.choice();
            updated_data = book.borrow_book(user_select,user_data,book_list)
            user_data = updated_data[0]
            book_list = updated_data[1]
            log_msg = updated_data[2]
            print(log_msg)

            #updating files according to change
            user.update(user_name,user_data)
            log.update(user_name,log_msg)
            book.update(book_list)
                
        elif user_choice == 2: #if user select to return
            display.heading("which book are you returning?")
            display.user_data(user_data)
            if len(user_data) != 0:
                user_select = user.choice();
                updated_data = book.return_book(user_select,user_data,book_list)
                user_data = updated_data[0]
                book_list = updated_data[1]
                log_msg = updated_data[2]
                print(log_msg)

                #updating files according to change
                user.update(user_name,user_data)
                log.update(user_name,log_msg)
                book.update(book_list)
                              
                    
        elif user_choice == 3:
            display.heading("here are your logs")
            log.read(user_name)
            
                
        elif user_choice == 4:
            display.heading("here are the rules")
            display.library_rule()
                
        elif user_choice == 5:
            display.heading("program ended")       
            run = False
                
        else:
            display.input_warning()
            invalid = True




