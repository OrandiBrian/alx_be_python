from datetime import datetime, timedelta, date

def display_current_datetime():
    """ Display the current date and time """
    c = datetime.now()
    current_date = c.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date(fut_date):
    """ Calculate the future date """
    c = datetime.now()
    future_date = c + timedelta(days=fut_date)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime() # display the current date and time
fut_date = int(input("Enter the number of days to add to the current date: ")) # get the number of days to add
calculate_future_date(fut_date) # calculate the future date