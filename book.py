import datetime


##setting the date
now = datetime.datetime.now()
date = str(now)[:10]


#function to return days passed from borrowed date
def days_passed(borrowed_date):
    today = datetime.datetime.strptime(date, "%Y-%m-%d")
    borrowed_date = datetime.datetime.strptime(borrowed_date, "%Y-%m-%d")
    return abs((borrowed_date - today).days)
    

##some function related to book
def borrow_book(index,user_data,book_list):
    index = index - 1
    new_book = [
                book_list[index][0],
                book_list[index][1],
                date
                ]
    #user_data updating
    user_data.append(new_book)
 
    ##updating the book_list
    book_list[index][2] = str(int(book_list[index][2]) - 1)

    ## sending message for recording in log file
    log_msg= "Borrowed '"+book_list[index][0]+"' on '"+date+"' at '"+book_list[index][-1]+"'."
    
    #creating 3d array to return two 2d array at once
    returning_data = [user_data,book_list,log_msg]
    
    return returning_data
    

def return_book(index,user_data,book_list):
    fine = "0"
    index = index - 1

    #code for whether customer get fined or not
    fine_days = days_passed(user_data[index][2]) - 10
    if fine_days > 0:
        fine = str(fine_days * 0.5);
    
    ##updating user_data
    del user_data[index]

    ##updating book_list
    book_list[index][2] = str(int(book_list[index][2]) + 1)
    
    ## sending message for recording in log file
    log_msg= "Returned '"+book_list[index][0]+"' on '"+date+"' and fine '$"+fine+"'."

    #creating 3d array to return two 2d array at once
    returning_data = [user_data,book_list,log_msg]

    return returning_data

def update(book_list):
    full_dir = "books_in_self.txt"
    file = open(full_dir,"w")
    for each in book_list:
        file.write(each[0]+',')
        file.write(each[1]+',')
        file.write(each[2]+',')
        file.write(each[3]+'\n')
    file.close()

    #print(user_data)
