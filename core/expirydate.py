from datetime import datetime, timedelta

def generate_date():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2035, 12, 31)
    date_range = (end_date - start_date).days
    random_days = random.randint(0, date_range)
    random_date = start_date + timedelta(days=random_days)
    return random_date