import random
from datetime import datetime, timedelta

def generate_random_datetime(start_date, end_date):
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    random_date_time = start_date + timedelta(seconds=random_seconds)
    return random_date_time

start_date_str = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
end_date_str = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")

start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')
end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')

random_date_time = generate_random_datetime(start_date, end_date)
print("Random date and time:", random_date_time)
