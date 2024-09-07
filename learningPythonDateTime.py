import datetime

# get the current date and time
now = datetime.datetime.now()

print(now)

# get current date
current_date = datetime.date.today()

print(current_date)


#datetime.datetime - represents a single point in time, including a date and a time.
#datetime.date - represents a date (year, month, and day) without a time.
#datetime.time - represents a time (hour, minute, second, and microsecond) without a date.
#datetime.timedelta - represents a duration, which can be used to perform arithmetic with datetime objects.
