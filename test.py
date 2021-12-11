from datetime import date, datetime, timedelta


# helper function, used to return the string of future dates
def after_today(num):
    today = date.today()
    future = today + timedelta(days=num)
    future_str = future.strftime("%m/%d/%Y")
    return future_str

print(after_today(1))