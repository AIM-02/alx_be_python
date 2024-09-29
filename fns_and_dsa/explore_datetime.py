from datetime import datetime, timedelta

def display_current_datetime():
    #get current date and time
    current_date = datetime.now()

    #fprmat the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time: {formatted_date}")

def calculate_future_date(days):
    #calculate future date by adding days
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)

    #fprmat the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"future date: {formatted_future_date}")
    
def main():
        #display current date and time
        display_current_datetime()
        #user input
        number_of_days=int(input("enter the number of days to add to current date: "))
        calculate_future_date(number_of_days)

if __name__ == "__main__":
    main()    