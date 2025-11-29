#imported function to be used to convert string into datetime format
import numpy as np

#function to be used later for unit tests
def days_left(user_input):

    #Convert the date provided by user into a DateTime format so that today's date can be subtracted from user's date
    convert_datetime = np.datetime64(user_input)
    today=np.datetime64('today') 
    days = convert_datetime - today

    #return the number of days left
    return days

#ask the user to input a date in YYYY-MM-DD format and print the number of days left
user_input = input("Enter a date in format YYYY-MM-DD")
print(f"Number of days left are {days_left(user_input)}.")