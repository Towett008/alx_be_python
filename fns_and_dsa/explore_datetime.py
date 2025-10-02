
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)

if __name__ == "__main__":
    display_current_datetime()
    days = int(input("Enter number of days to add: "))
    calculate_future_date(days)

