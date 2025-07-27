from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("\n Current date and time:", formatted_date)

def calculate_future_date():
   
    try:
        days_to_add = int(input("Enter number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future_date)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    print(" DateTime Explorer")
    display_current_datetime()
    calculate_future_date()

