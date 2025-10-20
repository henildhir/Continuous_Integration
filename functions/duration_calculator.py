import numpy as np

def days_left(user_input):
    convert_datetime = np.datetime64(user_input)
    today=np.datetime64('today') 
    days = convert_datetime - today
    return days

user_input = input("Enter a date in format YYYY-MM-DD")
print(f"Number of days left are {days_left(user_input)}")